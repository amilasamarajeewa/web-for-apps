import json,re,html
from pathlib import Path
from urllib.request import Request,urlopen
from datetime import datetime,timezone

DEV="https://play.google.com/store/apps/dev?id=6407847081352449241&hl=en_US"
OUT=Path("data/apps.json")

def fetch(url):
    req=Request(url,headers={"User-Agent":"Mozilla/5.0"})
    with urlopen(req,timeout=30) as r:return r.read().decode("utf-8","ignore")

def clean(s):
    return re.sub(r"\s+"," ",html.unescape(re.sub("<[^>]+>"," ",s))).strip()

def main():
    page=fetch(DEV)
    ids=[]
    for pattern in [r'/store/apps/details\?id=([^"&\\]+)',r'https://play\.google\.com/store/apps/details\?id=([^"&\\]+)']:
        for m in re.finditer(pattern,page):
            if m.group(1) not in ids: ids.append(m.group(1))
    apps=[]
    for pid in ids:
        url=f"https://play.google.com/store/apps/details?id={pid}&hl=en_US"
        try:
            p=fetch(url)
            title=re.search(r'<title>(.*?)</title>',p,re.I|re.S)
            desc=re.search(r'<meta name="description" content="([^"]*)"',p,re.I)
            icons=re.findall(r'https://play-lh\.googleusercontent\.com/[^"\\ ]+',p)
            apps.append({"name":clean(title.group(1)).replace(" - Apps on Google Play","") if title else pid,
                         "developer":"AS TechnoArt",
                         "short_description":html.unescape(desc.group(1)) if desc else "",
                         "url":url,"icon":icons[0] if icons else "","screenshots":[]})
        except Exception as e: print("skip",pid,e)
    old=json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {"apps":[]}
    if not apps: apps=old.get("apps",[])
    OUT.write_text(json.dumps({"updated_at":datetime.now(timezone.utc).isoformat(),"source":DEV,"apps":apps},ensure_ascii=False,indent=2),encoding="utf-8")
    print("Apps:",len(apps))

if __name__=="__main__":main()
