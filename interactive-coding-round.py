'''Python

Boilerplate Code (Python)
'''
from typing import List, Dict
# --- Data Models ---
class HttpResponse:
    def __init__(self):
        self.status_code = 200
class PickupWindow:
    def __init__(self, start_min: int, end_min: int):
        self.start_min = start_min
        self.end_min = end_min
class ListPickupWindowsResponse(HttpResponse):
    def __init__(self, windows: List[PickupWindow] = None):
        super().__init__()
        self.windows = windows if windows is not None else []
# --- Mocked Downstream Service ---
class KitchenConfigApiService:
    def __init__(self, mocked_response: ListPickupWindowsResponse):
        self.mocked_response = mocked_response

    def get_pickup_windows_for_restaurant(self, restaurant_id: int) -> ListPickupWindowsResponse:
        return self.mocked_response
    # --- Core Merger (to implement) ---
class WindowMergeService:
    def __init__(self, kitchen_api: KitchenConfigApiService):
        self.kitchen_api = kitchen_api

    def merge_windows(self, restaurant_id: int) -> List[Dict]:
        """
        Returns:
        List[Dict]: [{"start_min": int, "end_min": int}, ...] consolidated
        windows sorted by start.
        Notes:
        - Half-open intervals: [start, end)
        - Touching windows merge: next.start <= current_end
        - Ignore invalid windows where end <= start
        """
        result: List[Dict] = []
    # TODO:
    # 1) Fetch windows from API
    # 2) Filter invalid (end <= start)
    # 3) Sort by start_min
    # 4) Single pass merge using the touching-merge rule
    # 5) Return consolidated list
        return result

#Python
# --- Test Harness ---
def _print_result(test_name: str, expected, actual):
    status = "PASS" if expected == actual else "FAIL"
    print(f"[{status}] {test_name}")
    print(f" Expected: {expected}")
    print(f" Actual: {actual}\n")
def test_various_shapes():
    windows = [
    PickupWindow( 60, 120), # 1:00-2:00
    PickupWindow(110, 180), # overlaps
    PickupWindow(180, 240), # touches previous end -> merge
    PickupWindow(300, 360), # separate block
    PickupWindow(360, 420), # touches -> merge
    PickupWindow(500, 500), # invalid zero-length -> ignored
    PickupWindow(30, 40), # early short block
    PickupWindow(35, 45), # overlaps early short block
    ]
    mocked_api = KitchenConfigApiService(ListPickupWindowsResponse(windows))
    service = WindowMergeService(mocked_api)
    actual = service.merge_windows(restaurant_id=123)
    expected = [
    {"start_min": 30, "end_min": 45}, # merged early pair
    {"start_min": 60, "end_min": 240}, # merged triple
    {"start_min": 300, "end_min": 420}, # merged touch pair
    ]
    _print_result("Merges overlaps + touching + ignores invalid", expected,
    actual)
if __name__ == "__main__":
    test_various_shapes()