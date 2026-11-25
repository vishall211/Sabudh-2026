
class Solution:
    def simplifyPath(self, path):
        stack = []

        # Split the path using /
        folders = path.split("/")

        for folder in folders:

            if folder == "" or folder == ".":
                continue

            # Move one folder back
            elif folder == "..":
                if stack:
                    stack.pop()

            # Add folder name
            else:
                stack.append(folder)

        # Build the final path
        return "/" + "/".join(stack)


# Input data
path = "/home/user/Documents/../Pictures"

# Run the solution
solution = Solution()
result = solution.simplifyPath(path)

print("\nInput:", path)
print("Output:", result, "\n")
