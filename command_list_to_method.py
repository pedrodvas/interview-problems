def create_code(commands: list[str], args: list):
    for i in range(len(commands)):

        arguments = ", ".join(str(val) for val in args[i])
        if i == 0:
            print(f"sol = {commands[i]}({arguments})")
        else:
            print(f"print(sol.{commands[i]}({arguments}))")
create_code(["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"], 
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]])