import sys
import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        all_items = dirs + files  # Combine files and dirs
        all_items.sort()
        level = root.replace(startpath, '').count(os.sep)
        if(level == 0):
            continue
        indent = ' ' * 2 * (level - 1)
        basename = os.path.basename(root)
        relpath = os.path.relpath(root, start=startpath)
        if "d_" in root:
            continue
        if not os.path.exists(root+"/index.md"):
            continue
        print('{}- [{}]({}/index.md) '.format(indent, basename, relpath, basename))
        subindent = ' ' * 2 * (level)

        for item in all_items:
            if os.path.isdir(os.path.join(root,item)):
               continue #Directory - Skip printing here, it will be printed in the next loop of os.walk

            f = os.path.basename(item)  # Extract filename from the path
            if "d_" == f[:2]:
                continue
            if "index.md" in f:
                continue
            if ".md" not in f: 
                continue
            print('{}- [{}]({}/{}) '.format(subindent, f, relpath, f))


def main() -> int:
    # print("Any Header content\n")
    print("- [Introduction](introduction.md)\n")
    list_files('./docs')
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit