VENV = .venv
ACTIVATE = .venv/bin/activate

run: $(ACTIVATE)
    # run the script with scalene to profile, only profile the _processing functions
	source $(ACTIVATE) && scalene --profile-only _processing main.py

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
