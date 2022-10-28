import requests


def post_prediction_data(endpoint: str, payload: dict):
    r = requests.post(endpoint, json=payload, proxies={"http": "", "https": ""})
    result = r.json()
    print(result)
    return result


def post_process_result(result: dict):
    try:
        body = result["body"]
        return body["class"]
    except Exception as e:
        print(e)
        raise ValueError("Could not find the appropriate key class.")


def post_request_and_prepare_prediction(url: str, payload: dict):
    _result = post_prediction_data(url, payload)
    _result = post_process_result(_result)
    return _result


if __name__ == "__main__":
    test_data = {
        'Alcohol': 12.17, 'Malic': 1.45, 'Ash': 2.53, 'Alcalinity': 19.0,
        'Magnesium': 104.0, 'Phenols': 1.89, 'Flavanoids': 1.75,
        'Nonflavanoids': 0.45, 'Proanthocyanins': 1.03, 'Color': 2.95,
        'Hue': 1.45, 'Dilution': 2.23, 'Proline': 355.0
    }
    api_path = "http://127.0.0.1:5000/predict/"
    result = post_prediction_data(api_path, test_data)
    result = post_process_result(result)
    print(result)
