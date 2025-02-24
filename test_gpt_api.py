import json
import urllib.request
import urllib.error
import argparse

def get_response(url,
                 model,
                 sys_prompt,
                 usr_prompt,
                 api_key):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    request_body = {
        "model": model,
        "messages": [
            {"role": "system", "content": sys_prompt},  
            {"role": "user", "content": usr_prompt}
        ]
    }

    json_body = json.dumps(request_body).encode("utf-8")

    request = urllib.request.Request(url, data=json_body, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(request) as response:
            response_data = response.read().decode("utf-8")

        response_json = json.loads(response_data)
        choices = response_json.get("choices", [])
        if choices:
            return choices[0]["message"]["content"]
        else:
            raise Exception(f"No choices found in the response: {response_data}")

    except urllib.error.HTTPError as e:
        error_response = e.read().decode("utf-8")
        raise Exception(f"API request failed with status code {e.code}\nResponse: {error_response}")
    
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, required=True, help='What is the first number?')
    parser.add_argument('--model', type=str, required=True, help='What is the second number?')
    parser.add_argument('--sys-prompt', type=str, default='default system context.', help='Your system property.')
    parser.add_argument('--usr-prompt', type=str, default='hello, world', help='Your command.')   
    parser.add_argument('--api-key', type=str, help='Your API Key for llm service.')
    args = parser.parse_args()

    url = args.url
    model = args.model
    sys_prompt = args.sys_prompt
    usr_prompt = args.usr_prompt
    api_key = args.api_key

    response = get_response(url, model, sys_prompt, usr_prompt, api_key)
    print(response)
