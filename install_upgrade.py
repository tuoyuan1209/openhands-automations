#!/usr/bin/env python3
"""Update only local repository files after operator pauses Git Sync."""
import argparse,datetime,shutil
from pathlib import Path
SOURCE=Path(__file__).resolve().parent
p=argparse.ArgumentParser(); p.add_argument('--target',default='/home/teemo/project/teemo_project/openhands-automations'); p.add_argument('--apply',action='store_true'); a=p.parse_args(); dst=Path(a.target).resolve()
if dst==SOURCE or not (dst/'.git').exists(): raise SystemExit('Specify existing local automation Git repository')
paths=[x for x in SOURCE.rglob('*') if x.is_file() and '__pycache__' not in x.parts and (x.relative_to(SOURCE).parts[0] in {'automations','imports','workflows'} or x.name in {'README.md','install_upgrade.py'})]
print('Target:',dst,'files:',len(paths));
if not a.apply: raise SystemExit('Dry run; pause Git Sync and old jobs before --apply')
backup=dst.parent/('openhands-automations-backup-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')); backup.mkdir(mode=0o700)
for x in paths:
 r=x.relative_to(SOURCE); y=dst/r
 if y.exists(): z=backup/r; z.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(y,z)
 y.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(x,y)
print('Local backup:',backup); print('No remote commit/push or Canvas import performed. Review git diff and choose Git Sync OR portable JSON import.')
