"""Build native PF knowledge_package ZIPs and normalized update manifest v1."""
from pathlib import Path
import argparse,datetime,hashlib,json,zipfile
import yaml
ROOT=Path(__file__).resolve().parents[1]
REPOSITORY='WebTolk/pf-joomla-rest-api-knowledge'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def zip_files(output,base,files):
 with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for f in files:
   info=zipfile.ZipInfo(f.relative_to(base).as_posix(),date_time=(2026,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16
   data=f.read_bytes()
   if f.suffix in {'.md','.json','.yaml','.yml','.py','.txt'} or f.name in {'LICENSE','SHA256SUMS'}:data=data.replace(b'\r\n',b'\n')
   z.writestr(info,data)
 with zipfile.ZipFile(output) as z:assert z.testzip() is None
def main(a):
 bundle=json.loads((ROOT/'bundle.json').read_text(encoding='utf-8'));version=bundle['version'];tag='v'+version
 if a.version and a.version!=version:raise SystemExit('Requested release version differs from bundle.json')
 out=Path(a.output) if a.output else ROOT/'.dist'/version;out.mkdir(parents=True,exist_ok=True)
 manifest_path=ROOT/'updates/joomla-rest-api.json'
 previous=json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else {'subjects':[]}
 old={s['id']:s for s in previous['subjects']};subjects=[];checksums=[]
 for entry in bundle['packages']:
  folder=ROOT/entry['path'];m=yaml.safe_load((folder/'package.yaml').read_text(encoding='utf-8'))
  assert m['id']==entry['id'] and m['version']==version and m['type']=='knowledge_package'
  artifact=out/f"{m['id']}-{version}.zip"
  files=[folder/'package.yaml']+sorted(p for p in folder.rglob('*') if p.is_file() and p!=folder/'package.yaml')
  zip_files(artifact,folder,files);digest=sha(artifact);checksums.append((artifact.name,digest))
  item={'version':version,'channels':['stable'],'stability':'stable','prerelease':False,'released_at':bundle['released_at'],'yanked':False,'source':{'provider':'github','repository':REPOSITORY,'ref':tag},'release':{'changelog_url':f'https://raw.githubusercontent.com/{REPOSITORY}/{tag}/CHANGELOG.md'},'compatibility':{'tested_processforge':'1.2.0','requires_contracts':['normalized-update-manifest-v1','knowledge-package-zip']},'dependencies':[{'type':'knowledge_package','id':d,'version':version} for d in entry['dependencies']],'artifacts':[{'type':'knowledge_package','format':'zip','url':f'https://github.com/{REPOSITORY}/releases/download/{tag}/{artifact.name}','sha256':digest,'size':artifact.stat().st_size}],'changes':[{'breaking':False,'summary':'Portable Joomla REST knowledge, primary core 6.2.0; native package-owned payload and update sites.'}],'migration':{'required':False}}
  history=[x for x in old.get(m['id'],{}).get('versions',[]) if x['version']!=version]
  same=next((x for x in old.get(m['id'],{}).get('versions',[]) if x['version']==version),None)
  if same and same['artifacts'][0]['sha256']!=digest and not a.allow_unpublished_rebuild:raise SystemExit('Version artifact changed; bump version instead of replacing a published release: '+m['id'])
  subjects.append({'type':'knowledge_package','id':m['id'],'name':m['name'],'versions':history+[item]})
 manifest={'schema_version':1,'product':{'id':bundle['id']},'generated_at':bundle['released_at'],'channels':{'stable':{'latest':version}},'subjects':subjects}
 manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 (out/'joomla-rest-api.json').write_bytes(manifest_path.read_bytes())
 bundle_files=[]
 for name in ['packages','docs','templates','updates','evidence','tools']:
  bundle_files.extend(p for p in (ROOT/name).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.log'})
 bundle_files.extend(ROOT/name for name in ['README.md','LICENSE','NOTICE.md','CHANGELOG.md','bundle.json','requirements.txt'])
 full=out/f'pf-joomla-rest-api-knowledge-{version}.zip';zip_files(full,ROOT,sorted(bundle_files));checksums.append((full.name,sha(full)))
 (out/'SHA256SUMS').write_text(''.join(f'{h}  {name}\n' for name,h in sorted(checksums)),encoding='utf-8')
 print(json.dumps({'version':version,'package_archives':len(subjects),'bundle':full.name,'total_bytes':sum((out/name).stat().st_size for name,_ in checksums)}))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output');p.add_argument('--version');p.add_argument('--allow-unpublished-rebuild',action='store_true');main(p.parse_args())
