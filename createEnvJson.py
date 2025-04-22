import json

LAMBDA_FUNCTIONS = [
    "ApiFunction",
    "OrchestratorFunction",
    "SQLDocketIngestFunction",
    "SQLDocumentIngestFunction",
    "SQLCommentIngestFunction",
    "HTMSummaryIngestFunction",
    "OpenSearchCommentFunction",
    "OpenSearchTextExtractFunction",
]


def main():
    env_json = {function: {} for function in LAMBDA_FUNCTIONS}
    try:
        with open(".env", "r") as env:
            print("creating .env.json from .env file")
            for line in env:
                line = line.strip()
                if line.startswith("#"):
                    # skip commented out lines
                    continue
                line_components = line.split("=")
                key = line_components[0]
                value = "".join(line_components[1:])
                if line:
                    for function in LAMBDA_FUNCTIONS:
                        env_json[function][key] = value
    except FileNotFoundError:
        print("could not find .env file")
        exit(1)
    with open(".env.json", "w") as f:
        f.write(json.dumps(env_json, indent=2))
        print("created .env.json")


if __name__ == "__main__":
    main()
