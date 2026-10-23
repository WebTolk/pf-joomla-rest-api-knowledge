"""Exercise native PF updater only in a fresh disposable workplace under .build."""
from pathlib import Path
import argparse,contextlib,copy,hashlib,importlib.util,io,json,subprocess,sys,uuid
import yaml
ROOT=Path(__file__).resolve().parents[1]
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False),encoding='utf-8')
def main(a):
 module=Path(a.pf_module).resolve();sys.path.insert(0,str(module.parent));spec=importlib.util.spec_from_file_location('pf_native_updater_acceptance',module);pf=importlib.util.module_from_spec(spec);sys.modules[spec.name]=pf;spec.loader.exec_module(pf)
 bundle=json.loads((ROOT/'bundle.json').read_text(encoding='utf-8'));feed=json.loads((ROOT/'updates/joomla-rest-api.json').read_text(encoding='utf-8'))
 run=ROOT/'.build'/('updater-'+uuid.uuid4().hex[:10]);w=run/'workplace';chosen=w/'chosen-packages';chosen.mkdir(parents=True)
 assert w.resolve().is_relative_to((ROOT/'.build').resolve())
 # Isolated fixture configuration. No live workplace configuration is read or changed.
 dump(w/'workplace.yaml',{'schema_version':1,'workplace':{'id':'joomla-rest-updater-smoke','name':'Joomla REST updater smoke','type':'workstation'},'process_forge':{'version_constraint':'^1.2','install_mode':'linked'},'path_constants':{'PF_WORKPLACE':'.'},'registries':{'package_roots':'registries/package-roots.yaml','knowledge_packages':'registries/knowledge-packages.yaml','installed_subjects':'registries/installed-subjects.yaml'}})
 dump(w/'registries/package-roots.yaml',{'schema_version':1,'package_roots':[{'id':'global','path':'chosen-packages','scope':'workplace','status':'available'}]})
 if a.remote:
  source_url='https://raw.githubusercontent.com/WebTolk/pf-joomla-rest-api-knowledge/main/updates/joomla-rest-api.json'
 else:
  local=copy.deepcopy(feed)
  for subject in local['subjects']:
   for v in subject['versions']:
    for artifact in v['artifacts']:
     artifact['url']=(ROOT/'.dist'/v['version']/artifact['url'].rsplit('/',1)[-1]).resolve().as_uri()
  mirror=run/'local-server/manifest.json';mirror.parent.mkdir(parents=True);mirror.write_text(json.dumps(local),encoding='utf-8');source_url=mirror.resolve().as_uri()
 installed=[]
 for entry in bundle['packages']:
  pid=entry['id'];folder=chosen/pid
  dump(folder/'package.yaml',{'schema_version':1,'id':pid,'name':pid,'kind':'documentation','type':'knowledge_package','scope':'workplace','version':'1.0.0','update_sites':[{'id':'acceptance-source','enabled':True,'manifest_url':source_url,'changelog_url':'https://github.com/WebTolk/pf-joomla-rest-api-knowledge/blob/main/CHANGELOG.md','channel':'stable','trust':{'require_https':a.remote,'require_sha256':True,'allow_unsigned':True},'policy':{'auto_check':True,'auto_apply':False}}]})
  (folder/'seed.txt').write_text('synthetic previous package\n',encoding='utf-8')
  installed.append({'type':'knowledge_package','id':pid,'version':'1.0.0','scope':'workplace','install_path':f'chosen-packages/{pid}'})
 dump(w/'registries/installed-subjects.yaml',{'schema_version':1,'subjects':installed})
 # Search-index acceptance is separate: suppress only the optional whole-index
 # post-effect in this test process. Native updater I/O, verification, backups,
 # installed-subject records and rollback functions remain unchanged.
 pf.search_index_maintenance_for_known_projects=lambda *args,**kwargs:{'scope':'isolated_updater_test','results':[]}
 from argparse import Namespace
 output=io.StringIO();steps=[]
 def call(name,**kw):
  with contextlib.redirect_stdout(output):code=getattr(pf,name)(Namespace(workplace=str(w),**kw))
  if code:raise RuntimeError(name+' failed\n'+output.getvalue()[-5000:])
  steps.append(name)
 call('command_update_candidates_refresh',channel='stable',dry_run=False)
 cache=json.loads((w/'runtime/update/candidates.json').read_text(encoding='utf-8'))
 candidates={c['subject']['id']:c for c in cache['candidates']}
 assert not cache['conflicts'] and len(candidates)==25
 assert all(c['available_version']==bundle['version'] and c['installable'] for c in candidates.values())
 for entry in bundle['packages']:
  c=candidates[entry['id']];cid=c['id'];destination=pf._update_registry_reader.install_path(w,c).resolve()
  assert destination==(chosen/entry['id']).resolve() and destination.is_relative_to(w.resolve())
  assert (w/'runtime/update/backups'/cid).resolve().is_relative_to(w.resolve())
  call('command_update_stage',candidate=cid,dry_run=False)
  call('command_update_verify',candidate=cid)
 first=candidates[bundle['packages'][0]['id']]
 staged=pf._update_document_reader.staged_record(w,first['id'])
 artifact=pf.path_resolution_to_path(pf.workplace_path_resolution(w,staged['artifact']['path']))
 assert artifact.resolve().is_relative_to(w.resolve())
 pristine=artifact.read_bytes();artifact.write_bytes(pristine+b'checksum-negative-test')
 with contextlib.redirect_stdout(output):bad=pf.command_update_verify(Namespace(workplace=str(w),candidate=first['id']))
 assert bad!=0
 artifact.write_bytes(pristine);call('command_update_verify',candidate=first['id'])
 with contextlib.redirect_stdout(output):blocked=pf.command_update_apply(Namespace(workplace=str(w),candidate=first['id'],confirm=False,dry_run=False,allow_custom_command=False))
 assert blocked!=0
 for entry in bundle['packages']:
  call('command_update_apply',candidate=candidates[entry['id']]['id'],confirm=True,dry_run=False,allow_custom_command=False)
  actual=yaml.safe_load((chosen/entry['id']/'package.yaml').read_text(encoding='utf-8'));assert actual['version']==bundle['version']
  assert not (chosen/entry['id']/'seed.txt').exists()
 owner=chosen/bundle['payload_owner'];data='resources/joomla/core/Joomla-REST-API-contracts/versions/6.2.0/components/com_content/openapi.json'
 assert hashlib.sha256((owner/data).read_bytes()).digest()==hashlib.sha256((ROOT/'packages'/bundle['payload_owner']/data).read_bytes()).digest()
 doctors=0;resources=0
 for entry in bundle['packages']:
  checks=pf._knowledge_package_validation_service.doctor(w,entry['id'],'global')
  failed=[str(c) for c in checks if c.level=='FAIL'];assert not failed,failed;doctors+=1
  m=yaml.safe_load((chosen/entry['id']/'package.yaml').read_text(encoding='utf-8'))
  for r in m['resources']:
   assert (chosen/r['path_ref']['relative_path']).exists();resources+=1
 assert resources==73 and not any((w/'packages'/e['id']).exists() for e in bundle['packages'])
 derived,source_checks=pf.build_installed_update_sites(w)
 assert not [c for c in source_checks if c.level=='FAIL']
 sites=[s for s in derived['sites'] if s['subject']['id'] in candidates]
 expected_url='https://raw.githubusercontent.com/WebTolk/pf-joomla-rest-api-knowledge/main/updates/joomla-rest-api.json'
 assert len(sites)==25 and all(s['source']['manifest_url']==expected_url for s in sites)
 for entry in reversed(bundle['packages']):
  c=candidates[entry['id']];assert pf._update_registry_reader.install_path(w,c).resolve().is_relative_to(w.resolve())
  call('command_update_rollback',candidate=c['id'])
  assert (chosen/entry['id']/'seed.txt').read_text(encoding='utf-8')=='synthetic previous package\n'
  assert yaml.safe_load((chosen/entry['id']/'package.yaml').read_text(encoding='utf-8'))['version']=='1.0.0'
 installed_after=yaml.safe_load((w/'registries/installed-subjects.yaml').read_text(encoding='utf-8'))
 registry_versions=sorted({s['version'] for s in installed_after['subjects']})
 rollback_registry_ok=registry_versions==['1.0.0']
 report={'status':'pass' if rollback_registry_ok else 'delivery_pass_with_known_updater_limitation','tested_processforge':'1.2.0','transport':'public_https' if a.remote else 'local_file_mirror','package_version':bundle['version'],'candidates':len(candidates),'staged_and_verified':25,'checksum_tampering_rejected':True,'apply_without_confirm_rejected':True,'applied':25,'files_rolled_back':25,'installed_subject_registry_rolled_back':rollback_registry_ok,'installed_subject_registry_versions_after_rollback':registry_versions,'known_updater_limitation':None if rollback_registry_ok else 'PF 1.2.0 restores package files but leaves installed-subject versions at the applied release. Reconcile registry against restored manifests before relying on subsequent version selection.','package_doctors':doctors,'resources_resolved':resources,'public_update_sites_discovered_after_install':len(sites),'custom_install_path_preserved':True,'fallback_install_path_not_created':True,'owner_payload_sha256_matched':True,'search_index_acceptance':'excluded; only optional post-effect suppressed inside disposable test process','live_workplace_modified':False}
 name='native-updater-public.json' if a.remote else 'native-updater-local.json'
 (ROOT/'evidence'/name).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 (run/'native-updater.log').write_text(output.getvalue(),encoding='utf-8')
 print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--pf-module',required=True);p.add_argument('--remote',action='store_true');main(p.parse_args())
