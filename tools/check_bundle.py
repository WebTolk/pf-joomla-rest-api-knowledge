"""Check portable metadata, owned payload, dependencies, links and feed hashes."""
from pathlib import Path
import hashlib,json,re,sys,zipfile
import yaml
ROOT=Path(__file__).resolve().parents[1]
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def main():
 bundle=load(ROOT/'bundle.json');ids={p['id'] for p in bundle['packages']};assert len(ids)==25
 owner=bundle['payload_owner'];count=0;consumer_files=0;links=0
 for entry in bundle['packages']:
  folder=ROOT/entry['path'];m=yaml.safe_load((folder/'package.yaml').read_text(encoding='utf-8'));index=yaml.safe_load((folder/'indexes/resource-index.yaml').read_text(encoding='utf-8'))
  assert m['id']==entry['id'] and m['version']==bundle['version'] and m['type']=='knowledge_package'
  assert (folder/'README.md').is_file() and (folder/'LICENSE').is_file()
  assert set(m.get('dependencies',[]))<=ids
  assert {r['id'] for r in index['resources']}=={r['id'] for r in m['resources']}
  for r in m['resources']:
   ref=r['path_ref'];assert ref['registry']=='package_roots' and ref['id']=='global'
   p=Path(ref['relative_path']);assert not p.is_absolute() and '..' not in p.parts
   assert p.parts[0]==owner and (ROOT/'packages'/p).exists()
   assert next(x for x in index['resources'] if x['id']==r['id'])['path_ref']==ref
   count+=1
  assert m['update_sites'] and all('install_path' not in x.get('policy',{}) for x in m['update_sites'])
  assert all(x['manifest_url'].startswith('https://raw.githubusercontent.com/WebTolk/pf-joomla-rest-api-knowledge/') for x in m['update_sites'])
 assert count==73
 for folder in [ROOT/'packages',ROOT/'docs',ROOT/'templates',ROOT/'evidence',ROOT/'updates']:
  for f in folder.rglob('*'):
   if not f.is_file():continue
   assert not any(x in f.parts for x in ['.pf','__pycache__','.validation-deps'])
   if f.suffix not in {'.md','.json','.yaml','.yml'}:continue
   consumer_files+=1;s=f.read_text(encoding='utf-8')
   assert not re.search(r'(?<![A-Za-z0-9_-])[A-Za-z]:[\\/]',s),f'Private path: {f.relative_to(ROOT)}'
   if f.suffix=='.md':
    for link in re.findall(r'\]\(([^)]+)\)',s):
     if '://' in link:continue
     assert (f.parent/link.split('#')[0]).exists(),f'Broken link: {f.relative_to(ROOT)} -> {link}'
     links+=1
 feed_path=ROOT/'updates/joomla-rest-api.json';artifacts=0
 if feed_path.exists():
  feed=load(feed_path);assert {s['id'] for s in feed['subjects']}==ids
  for subject in feed['subjects']:
   assert subject['type']=='knowledge_package'
   item=next(v for v in subject['versions'] if v['version']==bundle['version'])
   assert 'install_path' not in item.get('update_policy',{})
   artifact=item['artifacts'][0];assert artifact['url'].startswith('https://github.com/WebTolk/pf-joomla-rest-api-knowledge/releases/download/v'+bundle['version']+'/')
   zip_path=ROOT/'.dist'/bundle['version']/artifact['url'].rsplit('/',1)[-1]
   if zip_path.exists():
    assert hashlib.sha256(zip_path.read_bytes()).hexdigest()==artifact['sha256']
    with zipfile.ZipFile(zip_path) as z:
     assert z.testzip() is None and 'package.yaml' in z.namelist()
     m=yaml.safe_load(z.read('package.yaml'));assert m['id']==subject['id'] and m['version']==item['version'] and m['type']==subject['type']
     assert all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist())
    artifacts+=1
 result={'status':'pass','packages':len(ids),'resources':count,'consumer_files':consumer_files,'relative_links':links,'local_artifacts_verified':artifacts,'primary_core_version':bundle['primary_joomla_version']}
 print(json.dumps(result));return result
if __name__=='__main__':main()
