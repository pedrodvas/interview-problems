def format_to_file_title(s):
    output = []
    for i in range(len(s)):
        output.append('-' if s[i]==' ' else s[i].lower())
    return "".join(output)+".py"
if __name__ == '__main__':
    print(format_to_file_title("Minimum Number of Steps to Make Two Strings Anagram"))