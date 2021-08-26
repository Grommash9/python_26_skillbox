import os


def gen_files_path(target_directory: str, base_dir: str = 'C:/'):
    for elements in os.listdir(base_dir):
        os.chdir(base_dir)
        if os.path.isdir(elements):
            if str(os.path.basename(elements)) == target_directory:
                yield os.path.abspath(elements)
                exit()
            else:
                yield from gen_files_path(target_directory, base_dir=os.path.abspath(elements))
        else:
            yield os.path.abspath(elements)


for path in gen_files_path(target_directory='plugins', base_dir='D:/'):
    print(path)



