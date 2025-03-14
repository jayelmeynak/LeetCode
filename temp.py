def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    strs.sort(key=lambda x: len(x), reverse=False)
    prefix = strs[0]
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

print(longestCommonPrefix(["flower", "flow", "flower"]))
 