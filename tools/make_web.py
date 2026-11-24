"""web/app.html (Artifact sürümü) → assets/web/index.html (uygulama içi, tam belge)."""
import os, shutil
R = os.path.join(os.path.dirname(__file__), '..')
body = open(os.path.join(R, 'site', 'app.html'), encoding='utf-8').read()
doc = ('<!doctype html>\n<html lang="tr">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}[hidden]{display:none!important}img{max-width:100%}</style>\n'
       '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
out = os.path.join(R, 'assets', 'web'); os.makedirs(out, exist_ok=True)
open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(doc)
shutil.copy(os.path.join(R, 'site', 'data.js'), os.path.join(out, 'data.js'))
shutil.copy(os.path.join(R, 'assets', 'icon_180.png'), os.path.join(out, 'icon.png'))
shutil.copy(os.path.join(R, 'assets', 'icon_180.png'), os.path.join(R, 'site', 'icon.png'))
print('ok', os.path.getsize(os.path.join(out, 'index.html')) // 1024, 'KB')
