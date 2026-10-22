"""Build the frostforge-legal GitHub Pages site.

Sources:
  - English and Portuguese: docs/legal/privacy-policy.md in the private game repo.
  - Spanish (Latin America, es-419): src/privacy-policy.es.md in this repo.

Usage: python3 build_legal.py <frostforge repo> <out dir> <controller name> <date> [<controller name in Spanish>]

Each page holds one <section lang="..."> per language. A small script shows one language at a
time (URL #hash or ?lang= > saved choice > browser language); without JavaScript all sections
stay visible.
"""
import json
import re
import shutil
import sys
from pathlib import Path

import markdown

src_repo, out, controller, date = sys.argv[1:5]
controller_es = sys.argv[5] if len(sys.argv) > 5 else re.sub(
    r"^the Frostforge developer, ", "el desarrollador de Frostforge, ", controller)
email = "playfrostforge@gmail.com"
DELETE_URL = "https://agspf94.github.io/frostforge-legal/delete-account.html"
out = Path(out)
here = Path(__file__).resolve().parent

LANGS = [  # (hash id, html lang, flag, label)
    ("en", "en", "\U0001F1FA\U0001F1F8", "EN"),
    ("pt-br", "pt-BR", "\U0001F1E7\U0001F1F7", "PT-BR"),
    ("es", "es-419", "\U0001F1EA\U0001F1F8", "ES"),
]
NAV = {
    "en": ("Home", "Privacy", "Delete account"),
    "pt-br": ("Início", "Privacidade", "Excluir conta"),
    "es": ("Inicio", "Privacidad", "Eliminar cuenta"),
}

md = Path(src_repo, "docs/legal/privacy-policy.md").read_text(encoding="utf-8")
# Drop the draft header and hosting proposal: keep from the first "# English".
md = md[md.index("# English"):]
# The game repo now also carries the Spanish section; prefer it over the local copy.
if "# Español (Latinoamérica)" in md:
    md, game_es = md.split("# Español (Latinoamérica)", 1)
    (here / "src/privacy-policy.es.md").write_text("# Español (Latinoamérica)" + game_es, encoding="utf-8")
md_es = (here / "src/privacy-policy.es.md").read_text(encoding="utf-8")
repl = {
    "`[DATE]`": date, "`[DATA]`": date, "`[FECHA]`": date,
    "`[PRIVACY EMAIL]`": email, "`[E-MAIL DE PRIVACIDADE]`": email, "`[CORREO DE PRIVACIDAD]`": email,
    "`[OWNER LEGAL NAME / CONTACT ENTITY]`": controller,
    "`[NOME LEGAL DO RESPONSÁVEL]`": controller,
    "`[NOMBRE LEGAL DEL RESPONSABLE]`": controller_es,
    "`[ACCOUNT DELETION URL]`": f"[{DELETE_URL}]({DELETE_URL})",
    "`[URL DE EXCLUSÃO DE CONTA]`": f"[{DELETE_URL}]({DELETE_URL})",
    "`[URL DE ELIMINACIÓN DE CUENTA]`": f"[{DELETE_URL}]({DELETE_URL})",
}
for k, v in repl.items():
    md = md.replace(k, v)
    md_es = md_es.replace(k, v)
left = re.findall(r"\[[A-Z][A-Z \-/ÇÁÉÍÓÚÃÕÑ]+\]", md + md_es)
assert not left, f"unfilled placeholders: {left}"

en_md, pt_md = md.split("# Português (Brasil)", 1)
en_md = re.sub(r"\n-{3,}\s*$", "\n", en_md.rstrip()).replace("# English", "# English {#en}", 1)
pt_md = re.sub(r"\n-{3,}\s*$", "\n", ("# Português (Brasil) {#pt-br}" + pt_md).rstrip())
es_md = md_es.replace("# Español (Latinoamérica)", "# Español (Latinoamérica) {#es}", 1)

CSS = """
:root{--bg:#f7f8fa;--fg:#1c2330;--muted:#5b6575;--card:#fff;--line:#dde2ea;--accent:#d9621f}
@media (prefers-color-scheme:dark){:root{--bg:#10141b;--fg:#e6e9ef;--muted:#9aa4b4;--card:#171c25;--line:#2a3140;--accent:#ff8a3d}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:860px;margin:0 auto;padding:32px 16px 64px}
header{display:flex;justify-content:space-between;align-items:baseline;gap:16px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:12px;margin-bottom:24px}
header nav a{color:var(--muted);text-decoration:none;margin-left:12px}header strong{font-size:1.2rem}
a{color:var(--accent)}h1{margin-top:40px}h2{margin-top:28px;font-size:1.15rem}
.table{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:.92rem;background:var(--card)}
th,td{border:1px solid var(--line);padding:8px;vertical-align:top;text-align:left}th{background:var(--bg)}
code{background:var(--card);border:1px solid var(--line);border-radius:4px;padding:0 4px;overflow-wrap:anywhere}
.box{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px 20px;margin:16px 0}
hr{border:0;border-top:1px solid var(--line);margin:40px 0}
.langs{display:none;gap:6px;flex-wrap:wrap;margin:0 0 8px}
.langs button{font:inherit;font-size:.9rem;color:var(--fg);background:var(--card);border:1px solid var(--line);border-radius:999px;padding:4px 12px;cursor:pointer;min-height:36px}
.langs button[aria-pressed="true"]{border-color:var(--accent);color:var(--accent);font-weight:600}
.langs button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.nojs-langs a{margin-right:10px}
.js .langs{display:flex}.js .nojs-langs{display:none}
.js section[data-lang]:not(.active),.js hr.sep{display:none}
.js section[data-lang]>h1:first-child{margin-top:16px}
"""

SCRIPT = """
(function(){
  var ids=%(ids)s, langs=%(langs)s, titles=%(titles)s, nav=%(nav)s, KEY='frostforge-lang';
  function norm(v){
    if(!v) return null; v=String(v).toLowerCase();
    if(v.indexOf('pt')===0) return 'pt-br';
    if(v.indexOf('es')===0) return 'es';
    if(v.indexOf('en')===0) return 'en';
    return null;
  }
  function fromUrl(){
    var h=location.hash.replace('#','').toLowerCase();
    if(ids.indexOf(h)>=0) return h;
    try{ return norm(new URLSearchParams(location.search).get('lang')); }catch(e){ return null; }
  }
  function saved(){ try{ return norm(localStorage.getItem(KEY)); }catch(e){ return null; } }
  function apply(id){
    document.querySelectorAll('section[data-lang]').forEach(function(s){
      s.classList.toggle('active', s.getAttribute('data-lang')===id);
    });
    document.querySelectorAll('.langs button').forEach(function(b){
      b.setAttribute('aria-pressed', b.getAttribute('data-lang')===id ? 'true' : 'false');
    });
    document.documentElement.lang=langs[id];
    if(titles[id]) document.title=titles[id];
    document.querySelectorAll('header nav a').forEach(function(a,i){
      a.textContent=nav[id][i];
      a.setAttribute('href', a.getAttribute('data-href')+(id==='en'?'':'#'+id));
    });
  }
  var start=fromUrl()||saved()||norm(navigator.language)||'en';
  apply(start);
  window.scrollTo(0,0);
  document.querySelectorAll('.langs button').forEach(function(b){
    b.addEventListener('click', function(){
      var id=b.getAttribute('data-lang');
      try{ localStorage.setItem(KEY,id); }catch(e){}
      try{ history.replaceState(null,'','#'+id); }catch(e){ location.hash=id; }
      apply(id); window.scrollTo(0,0);
    });
  });
  window.addEventListener('hashchange', function(){ var id=fromUrl(); if(id){ apply(id); window.scrollTo(0,0); } });
})();
"""


def wrap_tables(html):
    return re.sub(r"(<table>.*?</table>)", r'<div class="table">\1</div>', html, flags=re.S)


def page(titles, sections):
    """titles: {id: title}; sections: {id: html body}. English is the default/no-JS title."""
    import json
    buttons = "".join(
        f'<button type="button" data-lang="{i}" lang="{hl}" aria-pressed="{"true" if i == "en" else "false"}">'
        f'<span aria-hidden="true">{flag}</span> {label}</button>' for i, hl, flag, label in LANGS)
    nojs = "".join(f'<a href="#{i}" lang="{hl}">{label}</a>' for i, hl, _, label in LANGS)
    body = '\n<hr class="sep">\n'.join(
        f'<section data-lang="{i}" lang="{hl}">\n{wrap_tables(sections[i])}\n</section>' for i, hl, _, _ in LANGS)
    script = SCRIPT % {
        "ids": json.dumps([i for i, *_ in LANGS]),
        "langs": json.dumps({i: hl for i, hl, *_ in LANGS}),
        "titles": json.dumps(titles, ensure_ascii=False),
        "nav": json.dumps(NAV, ensure_ascii=False),
    }
    home, priv, dele = NAV["en"]
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titles["en"]}</title><style>{CSS}</style>
<script>document.documentElement.classList.add('js')</script></head>
<body><main><header><strong>Frostforge</strong><nav><a href="./" data-href="./">{home}</a><a href="privacy-policy.html" data-href="privacy-policy.html">{priv}</a><a href="delete-account.html" data-href="delete-account.html">{dele}</a></nav></header>
<div class="langs" role="group" aria-label="Language / Idioma">{buttons}</div>
<p class="nojs-langs">{nojs}</p>
{body}
</main>
<script>{script}</script>
</body></html>
"""


conv = lambda s: markdown.markdown(s, extensions=["tables", "attr_list"])
out.mkdir(parents=True, exist_ok=True)
(out / "privacy-policy.html").write_text(page(
    {"en": "Frostforge Privacy Policy", "pt-br": "Política de Privacidade do Frostforge",
     "es": "Política de Privacidad de Frostforge"},
    {"en": conv(en_md), "pt-br": conv(pt_md), "es": conv(es_md)}), encoding="utf-8")

delete_en = f"""
# Delete your Frostforge account and data {{#en}}

<div class="box" markdown="1">

**In the game (fastest):** open **Menu → Delete account** and confirm. Your save, your Google link, your sign-in
record and your feedback are removed immediately. This cannot be undone.

**Without the app** (for example, if you uninstalled it): email **[{email}](mailto:{email}?subject=Frostforge%20account%20deletion)**
with the subject "Frostforge account deletion". Guest accounts have no name or email, so include anything that helps us find
your account: the approximate date and time you last played, your device model, or a feedback id. We answer within 30 days.

</div>

**What is deleted:** game state (base, resources, research, heroes, troops), account id, Google link, sign-in record,
feedback messages and usage statistics.

**What may remain for a short time:** technical logs (up to 30 days), production backups (up to 35 days), and a copy of
feedback emailed to the developer inbox (deleted on request). Details: [Privacy Policy](privacy-policy.html).
"""
delete_pt = f"""
# Excluir sua conta e seus dados do Frostforge {{#pt-br}}

<div class="box" markdown="1">

**No jogo (mais rápido):** abra **Menu → Excluir conta** e confirme. Seu progresso, o vínculo com o Google, seu registro
de login e seus feedbacks são removidos na hora. Não pode ser desfeito.

**Sem o app** (por exemplo, se você desinstalou): envie um e-mail para **[{email}](mailto:{email}?subject=Exclus%C3%A3o%20de%20conta%20Frostforge)**
com o assunto "Exclusão de conta Frostforge". Contas de convidado não têm nome nem e-mail, então informe o que ajudar a
encontrar sua conta: data e hora aproximadas em que jogou pela última vez, modelo do aparelho ou o id de um feedback.
Respondemos em até 30 dias.

</div>

**O que é excluído:** estado do jogo (base, recursos, pesquisas, heróis, tropas), id da conta, vínculo com o Google,
registro de login, mensagens de feedback e estatísticas de uso.

**O que pode permanecer por pouco tempo:** logs técnicos (até 30 dias), backups de produção (até 35 dias) e a cópia do
feedback enviada por e-mail ao desenvolvedor (apagada mediante pedido). Detalhes: [Política de Privacidade](privacy-policy.html#pt-br).
"""
delete_es = f"""
# Eliminar tu cuenta y tus datos de Frostforge {{#es}}

<div class="box" markdown="1">

**En el juego (lo más rápido):** abre **Menú → Eliminar cuenta** y confirma. Tu partida, tu vínculo con Google, tu registro
de inicio de sesión y tus comentarios se eliminan de inmediato. No se puede deshacer.

**Sin la app** (por ejemplo, si la desinstalaste): escribe a **[{email}](mailto:{email}?subject=Eliminaci%C3%B3n%20de%20cuenta%20Frostforge)**
con el asunto "Eliminación de cuenta Frostforge". Las cuentas de invitado no tienen nombre ni correo, así que incluye todo lo que
nos ayude a encontrar tu cuenta: la fecha y hora aproximadas en que jugaste por última vez, el modelo de tu dispositivo o el id de un
comentario. Respondemos en un plazo de 30 días.

</div>

**Qué se elimina:** estado del juego (base, recursos, investigaciones, héroes, tropas), id de la cuenta, vínculo con Google,
registro de inicio de sesión, comentarios y estadísticas de uso.

**Qué puede permanecer por poco tiempo:** registros técnicos (hasta 30 días), copias de seguridad de producción (hasta 35 días) y la
copia de los comentarios enviada por correo al desarrollador (se elimina si lo solicitas). Detalles: [Política de Privacidad](privacy-policy.html#es).
"""
dconv = lambda s: markdown.markdown(s, extensions=["attr_list", "md_in_html"])
# Self-service deletion page (#850, #865): when the game repo has docs/legal/web/ with a filled config
# (prod apiBase/hostedUi/clientId from the stack outputs), publish that page and its config as-is.
# Otherwise fall back to the static instructions page below.
web = Path(src_repo, "docs/legal/web")
web_cfg = web / "delete-account-config.json"
if (web / "delete-account.html").exists() and web_cfg.exists() and all(
        json.loads(web_cfg.read_text(encoding="utf-8")).get(k) for k in ("apiBase", "hostedUi", "clientId")):
    shutil.copyfile(web / "delete-account.html", out / "delete-account.html")
    shutil.copyfile(web_cfg, out / "delete-account-config.json")
else:
    (out / "delete-account.html").write_text(page(
        {"en": "Delete Frostforge Account", "pt-br": "Excluir conta do Frostforge", "es": "Eliminar cuenta de Frostforge"},
        {"en": dconv(delete_en), "pt-br": dconv(delete_pt), "es": dconv(delete_es)}), encoding="utf-8")

index = {
    "en": f"""
# Frostforge {{#en}}

A factory-building strategy game for Android, in development.

- [Privacy Policy](privacy-policy.html)
- [Delete your account and data](delete-account.html)
- Support: [{email}](mailto:{email})
""",
    "pt-br": f"""
# Frostforge {{#pt-br}}

Um jogo de estratégia e construção de fábricas para Android, em desenvolvimento.

- [Política de Privacidade](privacy-policy.html#pt-br)
- [Excluir conta e dados](delete-account.html#pt-br)
- Suporte: [{email}](mailto:{email})
""",
    "es": f"""
# Frostforge {{#es}}

Un juego de estrategia y construcción de fábricas para Android, en desarrollo.

- [Política de Privacidad](privacy-policy.html#es)
- [Eliminar cuenta y datos](delete-account.html#es)
- Soporte: [{email}](mailto:{email})
""",
}
(out / "index.html").write_text(page(
    {"en": "Frostforge", "pt-br": "Frostforge", "es": "Frostforge"},
    {k: markdown.markdown(v, extensions=["attr_list"]) for k, v in index.items()}), encoding="utf-8")
(out / ".nojekyll").write_text("", encoding="utf-8")
(out / "README.md").write_text(
    "# frostforge-legal\n\nPublic pages for the Frostforge game (privacy policy, account deletion), served by GitHub Pages\n"
    "at https://agspf94.github.io/frostforge-legal/ in English, Portuguese (Brazil) and Spanish (Latin America).\n\n"
    "## Sources\n\n"
    "- English, Portuguese and Spanish: `docs/legal/privacy-policy.md` in the private game repo (the build copies the Spanish section into `src/privacy-policy.es.md`).\n"
    "- Account deletion: `docs/legal/web/delete-account.html` and its `delete-account-config.json` in the game repo, published as-is\n"
    "  once the config holds the prod values; otherwise a static page whose texts live in `build_legal.py`, like the index texts.\n\n"
    "Edit the sources, never the generated HTML.\n\n"
    "## Rebuild\n\n"
    "Needs Python 3 and `pip install markdown`. From this repo, with the game repo checked out next to it:\n\n"
    "```sh\n"
    "python3 build_legal.py ../frostforge . \"the Frostforge developer, Anderson Fantin\" \"YYYY-MM-DD\"\n"
    "```\n\n"
    "An optional fifth argument sets the controller name in Spanish (default: derived from the English one).\n"
    "The build fails if any `[PLACEHOLDER]` is left unfilled. Commit and push to `main`; GitHub Pages redeploys.\n\n"
    "## Languages\n\n"
    "Each page shows one language at a time, chosen by `#en` / `#pt-br` / `#es` (or `?lang=`), then the saved\n"
    "choice, then the browser language. Without JavaScript all languages are shown.\n", encoding="utf-8")
print("ok", sorted(p.name for p in out.iterdir()))
