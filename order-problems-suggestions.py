def index_list(separated_list: list[str]):
    return_list = []
    for i in separated_list:
        return_list.append(i.split(" "))
    return return_list

def pretty_string_creator(indexed_list: list[list[str]]):
    lines_list = []
    for line in indexed_list:
        pretty_line = " ".join(line)
        lines_list.append(pretty_line)
    return "\n".join(lines_list)
        
if __name__ == "__main__":
    problems = """1347: Minimum Number of Steps to Make Two Strings Anagrams ok
1383: Maximum Performance of a Team (ou variantes) ok
981: Time Based Key-Value Store ok
207: Course Schedule ok
146: LRU Cache ok
200: Number of Islands probably ok
56: Merge Intervals ok
1011: Capacity To Ship Packages Within D Days ok
1244: Design A Leaderboard LOCKED
394: Decode String ok
1235: Maximum Profit in Job Scheduling ok
743: Network Delay Time ok
23: Merge k Sorted Lists HALF ok
42: Trapping Rain Water ok
1166: Design File System LOCKED
1359: Count All Valid Pickup and Delivery Options ok
1229: Meeting Scheduler LOCKED
787: Cheapest Flights Within K Stops ok
239: Sliding Window Maximum ok 
72: Edit Distance ok
210: Course Schedule II ok"""
    separated_list = problems.split("\n")
    print(len(separated_list))
    print(separated_list)
    indexed_list = index_list(separated_list)
    print(len(indexed_list))
    print(f"indexed list is {indexed_list}")
    indexed_list.sort(key=lambda x: int(x[0][0:-1]))
    print(f"sorted list is {indexed_list}")
    print(pretty_string_creator(indexed_list))