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
        windows = self.kitchen_api.get_pickup_windows_for_restaurant(restaurant_id)
        print(f"windows are {windows.windows}")
        for i in range(len(windows.windows)):
            print(f"windows: {windows.windows[i].start_min} to {windows.windows[i].end_min}")
        
        #data acquired successfully, now we have to actually process it
        windows_list = _merge_windows(windows.windows)
        print(f"==========================")
        print(f"ordered windows:")
        for i in range(len(windows_list)):
            print(f"windows: {windows_list[i].start_min} to {windows_list[i].end_min}")
        
        print("==============================")
        merged_windows = []
        #now we have to merge the actual windows
        i = 0
        while i<len(windows_list):
            if windows_list[i].start_min >= windows_list[i].end_min:
                i += 1
                continue
            curr = i + 1
            new_window = PickupWindow(windows_list[i].start_min, windows_list[curr-1].end_min)
            while curr < len(windows_list) and new_window.end_min >= windows_list[curr].start_min:
                print(f"window 1: {windows_list[i].start_min} to {windows_list[i].end_min}")
                print(f"window 2: {windows_list[curr].start_min} to {windows_list[curr].end_min}")
                new_window = PickupWindow(windows_list[i].start_min, windows_list[curr].end_min)
                curr += 1
            
            merged_windows.append(new_window)
            i = curr
        
        formatted_windows = []
        for i in range(len(merged_windows)):
            formatted_windows.append({})
            formatted_windows[-1]["start_min"] = merged_windows[i].start_min
            formatted_windows[-1]["end_min"] = merged_windows[i].end_min
            print(f"windows merged: {merged_windows[i].start_min} to {merged_windows[i].end_min}")
        
        #formatting

        return formatted_windows

def _merge_windows(windows: List[PickupWindow]):
    if len(windows) == 1:
        return windows
    middle = len(windows)//2
    
    left_part = _merge_windows(windows[middle:])
    right_part = _merge_windows(windows[:middle])

    return_list = []
    left_iterator = 0
    right_iterator = 0

    while left_iterator + right_iterator < len(left_part) + len(right_part):
        if right_iterator==len(right_part):
            return_list.append(left_part[left_iterator])
            left_iterator += 1
        elif left_iterator == len(left_part):
            return_list.append(right_part[right_iterator])
            right_iterator += 1        
        elif left_part[left_iterator].start_min < right_part[right_iterator].start_min:
            return_list.append(left_part[left_iterator])
            left_iterator += 1
        else:
            return_list.append(right_part[right_iterator])
            right_iterator += 1
    
    return return_list

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