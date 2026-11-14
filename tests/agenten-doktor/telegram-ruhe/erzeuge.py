import importlib.machinery, importlib.util, sys, yaml
quelle, ziel = sys.argv[1], sys.argv[2]
lo = importlib.machinery.SourceFileLoader("d", quelle)
spec = importlib.util.spec_from_loader("d", lo); d = importlib.util.module_from_spec(spec); lo.exec_module(d)
k = {"MODELL_ANBIETER": "openrouter", "DOMAIN": "test.invalid", "EIGENTUEMER_TELEGRAM_ID": "4711"}
cfg = d.hermes_config("kurt", {"telegram": True, "werkzeuge": ["veroeffentlichen", "vorschlag"]}, k, {"raeume": {}})
# Nur fuer den Test: Rocket.Chat-Plugin gibt es im nackten Image nicht, Telegram geht an die Attrappe.
cfg["plugins"] = {"enabled": [], "disabled": []}
cfg["platforms"].pop("rocketchat", None)
cfg["platforms"].setdefault("telegram", {})["extra"] = {"base_url": "http://tgattrappe:8081/bot", "base_file_url": "http://tgattrappe:8081/file/bot"}
open(ziel, "w").write(yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False))
print(ziel, "telegram:", cfg["platforms"]["telegram"], "| display.telegram:", cfg["display"]["platforms"]["telegram"])
