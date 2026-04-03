class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        paths = []

        for part in parts:
            if part == "" or part == ".":
                continue

            if part == "..":
                if paths:
                    paths.pop()
            else:
                paths.append(part)

        return "/" + "/".join(paths)