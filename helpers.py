from typing import List, Dict

def prompt_nonempty(label: str) -> str:
    while True:
        val = input(label).strip()
        if val:
            return val
        print("Value cannot be empty. Try again.")

def find_by_key(data: List[Dict], key: str, value: str):
    for item in data:
        if str(item.get(key)) == str(value):
            return item
    return None

def ensure_unique(data: List[Dict], key: str, value: str) -> bool:
    return find_by_key(data, key, value) is None

def show_all(data: List[Dict], title: str):
    print(f"--- {title} ---")
    if not data:
        print("No records found.")
    else:
        for d in data:
            print(d)
    print("-------------------------")

def search_keyword(data: List[Dict], keys: List[str], keyword: str) -> List[Dict]:
    keyword = keyword.lower()
    results = []
    for item in data:
        for k in keys:
            val = str(item.get(k, "")).lower()
            if keyword in val:
                results.append(item)
                break
    return results

