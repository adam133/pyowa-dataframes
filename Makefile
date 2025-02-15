VENV = .venv
ACTIVATE = .venv/bin/activate

run: $(ACTIVATE)
	source $(ACTIVATE) && scalene main.py

clean:
	rm -rf profile.json profile.html
	rm -rf resources
	rm -rf .venv
	rm -rf outputs

$(ACTIVATE): $(VENV)
venv:
	uv venv
	uv sync

.PHONY: run profile clean
