import json
from typing import Any


def write_json(output: dict[str, Any], filename: str, caller: str):
    output_filename = filename.split("/")[-1].split(".")[0] + "_" + caller + ".json"
    with open("outputs/" + output_filename, "w") as f:
        json.dump(output, f)
