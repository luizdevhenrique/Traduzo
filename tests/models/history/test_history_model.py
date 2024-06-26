import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    response = HistoryModel.list_as_json()
    data = json.loads(response)

    expected_data = [
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        }
        ]

    for item in data:
        item.pop("_id", None)

    assert data == expected_data, f"Expected {expected_data}, but got {data}"
