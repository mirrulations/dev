import sys
import json
import boto3
import pathlib


def generate_payload(path) -> str:
    payload = {
        "Records": [
            {
                "eventVersion": "2.0",
                "eventSource": "aws:s3",
                "awsRegion": "us-east-1",
                "eventTime": "1970-01-01T00:00:00.000Z",
                "eventName": "ObjectCreated:Put",
                "userIdentity": {"principalId": "EXAMPLE"},
                "requestParameters": {"sourceIPAddress": "127.0.0.1"},
                "responseElements": {
                    "x-amz-request-id": "EXAMPLE123456789",
                    "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH",
                },
                "s3": {
                    "s3SchemaVersion": "1.0",
                    "configurationId": "testConfigRule",
                    "bucket": {
                        "name": "mirrulations",
                        "ownerIdentity": {"principalId": "EXAMPLE"},
                        "arn": "arn:aws:s3:::mirrulations",
                    },
                    "object": {
                        "key": f"{path}",
                        "size": 1024,
                        "eTag": "0123456789abcdef0123456789abcdef",
                        "sequencer": "0A1B2C3D4E5F678901",
                    },
                },
            }
        ]
    }
    return payload


def get_s3_path_from_filepath(file: pathlib.Path) -> str:
    filepath = file.name
    if filepath.endswith(".htm"):
        #ACF-2025-0004-0001_content.htm
        split_file = filepath.split("-")
        agency = split_file[0]
        docket_id = "-".join(
            split_file[:-1]
        )  # join everything but the last element in the list
        type = "documents"

    elif filepath.endswith(".json"):
        with open(file, "r") as f:
            data = json.load(f)
            type = data["data"]["type"]
            attributes = data["data"]["attributes"]

            agency = attributes["agencyId"]

            if type == "dockets":
                type = "docket"
                docket_id = data["data"]["id"]
            else:
                docket_id = attributes["docketId"]
    else:
        return None
    return f"raw-data/{agency}/{docket_id}/text-{docket_id}/{type}/{filepath}"


def invoke_local_lambda(payload: str) -> None:
    lambda_client = boto3.client("lambda", endpoint_url="http://localhost:3001")
    lambda_client.invoke(
        FunctionName="OrchestratorFunction",
        Payload=bytes(json.dumps(payload), encoding="utf-8"),
    )


def main():
    """
    Main function to execute the file reading.  Prompts the user for a
    filepath, reads the file, and prints the contents.
    """
    if len(sys.argv) > 1:
        filepath = sys.argv[1]  # Get filepath from command line argument
    else:
        print("Please enter a filepath")

    filepath = pathlib.Path(filepath)

    s3_path = get_s3_path_from_filepath(filepath)
    payload = generate_payload(s3_path)

    invoke_local_lambda(payload)


if __name__ == "__main__":
    main()
