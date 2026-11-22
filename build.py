"""Ģenerē profilu lapas no app.template.html. Palaid: python3 build.py"""
import json, os
PROFILES = [("silvestrs", "Silvestrs", "Silvestr"), ("sintija", "Sintija", "Sintij")]
tpl = open("app.template.html", encoding="utf-8").read()
for slug, name, voc in PROFILES:
    os.makedirs(slug, exist_ok=True)
    html = tpl.replace("{{P}}", slug).replace("{{VOC}}", voc).replace("{{NAME}}", name)
    open(f"{slug}/index.html", "w", encoding="utf-8").write(html)
    man = json.load(open("manifest.json", encoding="utf-8"))
    man.update(name=f"Rutīna · {name}", start_url="./", scope="./",
               icons=[dict(i, src="../" + i["src"]) for i in man["icons"]])
    json.dump(man, open(f"{slug}/manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("ok")
