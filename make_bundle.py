"""Build demo-bundle.js from a local lab-trace repo: every commit touching STATE.md, with the
markdown files and directory listings at each commit. Images are referenced by path (ship them
as supporting files next to index.html)."""
import subprocess, json, sys, os
repo=sys.argv[1]; name=sys.argv[2]; out=sys.argv[3] if len(sys.argv)>3 else 'demo-bundle.js'
def git(*a): return subprocess.run(['git','-C',repo]+list(a),capture_output=True,text=True).stdout
log=[l.split('|',2) for l in git('log','--reverse','--format=%H|%aI|%s','--','STATE.md').strip().splitlines()]
FILES=['STATE.md','REASONING.md','RESOURCES.md','agent/FEEDBACK.md','agent/CHECKS.md','agent/INFLIGHT.md','agent/RECALL.md','agent/PITFALLS.md','states/README.md']
files={};dirs={};images=set()
for sha,date,msg in log:
    tree=git('ls-tree','-r','--name-only',sha).split()
    f={}
    for path in [t for t in tree if t.endswith('.md') and (t in FILES or t.startswith('states/'))]:
        f[path]=git('show',f'{sha}:{path}')
    files[sha]=f; dirs[sha]={'states':sorted(os.path.basename(t) for t in tree if t.startswith('states/') and t.endswith('.md'))}
    images.update(t for t in tree if t.startswith('evidence/') and t.endswith('.png'))
bundle={'repo':name,'commits':[{'sha':s,'date':d,'msg':m} for s,d,m in log],'files':files,'dirs':dirs,'images':{p:p for p in sorted(images)}}
open(out,'w').write('window.LT_DEMO='+json.dumps(bundle)+';'); print(f'{out}: {len(log)} commits, {sum(len(v) for v in files.values())} files, {len(images)} images, {os.path.getsize(out)/1e6:.1f} MB')
