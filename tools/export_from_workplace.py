"""Export the authorized Joomla knowledge corpus; never export workplace runtime."""
from pathlib import Path
import argparse,copy,datetime,importlib.util,json,os,shutil,sys
import yaml
ROOT=Path(__file__).resolve().parents[1]
OWNER='joomla.rest-api.documentation'
REPOSITORY='WebTolk/pf-joomla-rest-api-knowledge'

def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False),encoding='utf-8')
def main(a):
 w=Path(a.workplace);corpus=Path(a.corpus);pf_path=Path(a.pf_module)
 sys.path.insert(0,str(pf_path.parent));spec=importlib.util.spec_from_file_location('pf_knowledge_export',pf_path);pf=importlib.util.module_from_spec(spec);sys.modules[spec.name]=pf;spec.loader.exec_module(pf)
 pids=[OWNER]+sorted(p.name for p in (w/'packages').glob('joomla.rest-api.*') if p.is_dir() and p.name!=OWNER)
 assert len(pids)==25
 payload=ROOT/'packages'/OWNER/'resources/joomla/core'
 target=payload/'Joomla-REST-API-contracts';target.mkdir(parents=True,exist_ok=True)
 for name in ['common','versions']:shutil.copytree(corpus/name,target/name,dirs_exist_ok=True)
 for name in ['README.md','validation.json','behaviour-validation.json','coverage-summary.json']:shutil.copy2(corpus/name,target/name)
 shutil.copytree(corpus.parent/'Joomla-REST-API-docs',payload/'Joomla-REST-API-docs',dirs_exist_ok=True)
 shutil.copy2(corpus.parent/'Joomla-core/6.x/6.2.0/LICENSE.txt',ROOT/'LICENSE')
 for name in ['validation.json','behaviour-validation.json']:
  shutil.copy2(corpus/name,ROOT/'evidence'/('rest-'+name))
 shutil.copy2(corpus/'reports/current-api-audit-6.2.0.json',ROOT/'evidence/api-audit-6.2.0.json')
 fixture=ROOT/'.build/index-workplace';fixture.mkdir(parents=True,exist_ok=True)
 dump(fixture/'workplace.yaml',{'schema_version':1,'registries':{'package_roots':'registries/package-roots.yaml'},'path_constants':{'PF_WORKPLACE':'.'}})
 dump(fixture/'registries/package-roots.yaml',{'schema_version':1,'package_roots':[{'id':'global','path':str(ROOT/'packages'),'scope':'workplace','status':'available'}]})
 entries=[]
 for pid in pids:
  original=w/'packages'/pid/'package.yaml';m=yaml.safe_load(original.read_text(encoding='utf-8-sig'))
  m.update(version=a.version,type='knowledge_package',status='released',package_root='global')
  m['dependencies']=[] if pid==OWNER else [OWNER] if pid.endswith('.common') else [OWNER,'joomla.rest-api.common']
  m['update_sites']=[{'id':'webtolk-joomla-rest-stable','enabled':True,'manifest_url':f'https://raw.githubusercontent.com/{REPOSITORY}/main/updates/joomla-rest-api.json','changelog_url':f'https://raw.githubusercontent.com/{REPOSITORY}/main/CHANGELOG.md','channel':'stable','priority':10,'trust':{'require_https':True,'require_sha256':True,'allow_unsigned':True,'signature_required':False},'policy':{'check_interval_hours':24,'auto_check':True,'auto_stage':False,'auto_apply':False,'notify_operator':True,'allow_stage':True,'allow_apply':True,'backup_before_apply':True}}]
  for r in m['resources']:
   previous=r['path_ref'];assert previous['registry']=='knowledge_roots' and previous['id']=='local-docs'
   r['path_ref']={'registry':'package_roots','id':'global','relative_path':OWNER+'/resources/'+previous['relative_path']}
   r['source']={'kind':'local_mirror','root':'global'}
   r['license']={'id':'GPL-2.0-or-later','notice':'Joomla-derived metadata; see repository LICENSE and NOTICE.md.'}
  pf._update_schema_checks.require(m,'package-manifest.schema.json',pid)
  dest=ROOT/'packages'/pid;dump(dest/'package.yaml',m)
  index=pf._package_manifest_writer.build_index(m,fixture,'global')
  pf._update_schema_checks.require(index,'knowledge-resource-index.schema.json',pid+' index')
  dump(dest/'indexes/resource-index.yaml',index)
  for name in ['LICENSE','NOTICE.md']:shutil.copy2(ROOT/name,dest/name)
  guide=f'https://github.com/{REPOSITORY}/blob/v{a.version}'
  lines=[f'# {pid}','',f'Пакет знаний ProcessForge. Версия пакета: {a.version}. Основной выпуск Joomla: 6.2.0.','',m['description'],'','## Использование','',f'[Установка и обновление]({guide}/README.md). [Структура пакетов]({guide}/docs/knowledge-package-layout.md). [Лицензия](LICENSE).','', 'Зависимости: '+(', '.join(m['dependencies']) or 'нет')+'.','', 'Владелец файлов корпуса: '+OWNER+'. Корень пакетов: логический global; физический путь выбирается при установке.','','## Ресурсы','','| Resource ID | Версия данных | Содержимое |','|---|---|---|']
  for r in m['resources']:
   data=ROOT/'packages'/r['path_ref']['relative_path'];link=Path(os.path.relpath(data,dest)).as_posix()
   if data.is_dir():link+='/README.md'
   lines.append(f"|{pid}:{r['id']}|{r.get('version','')}|[{r['title']}]({link})|")
  lines+=['','## Обновление','','update_sites в package.yaml указывает на общий штатный сервер обновлений PF. Применение заменяет весь каталог пакета; пользовательские заметки храните отдельно. Пакеты устанавливаются в порядке: documentation, common, компоненты. Версии 5.4.8/6.1.3 архивные; для новой работы выбирать contract-6-2-0.']
  (dest/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
  entries.append({'id':pid,'version':a.version,'path':f'packages/{pid}','resources':len(m['resources']),'dependencies':m['dependencies']})
 bundle={'schema_version':1,'id':'webtolk.joomla-rest-api-knowledge','version':a.version,'released_at':datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z'),'primary_joomla_version':'6.2.0','archived_joomla_versions':['5.4.8','6.1.3'],'payload_owner':OWNER,'package_root_id':'global','packages':entries,'format_note':'Repository inventory; native installation subjects and update manifest use the ProcessForge contract.'}
 (ROOT/'bundle.json').write_text(json.dumps(bundle,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'packages':len(entries),'resources':sum(x['resources'] for x in entries),'version':a.version,'payload_owner':OWNER}))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--workplace',required=True);p.add_argument('--corpus',required=True);p.add_argument('--pf-module',required=True);p.add_argument('--version',default='1.1.0');main(p.parse_args())
