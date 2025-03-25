import os

def replace_space_with_underscore(root_dir):
    # 하위 디렉토리부터 처리하면 폴더 이름 변경 시 경로 문제를 방지할 수 있습니다.
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # 파일 이름 변경
        for filename in filenames:
            if " " in filename:
                new_filename = filename.replace(" ", "_")
                old_file = os.path.join(dirpath, filename)
                new_file = os.path.join(dirpath, new_filename)
                # 충돌 방지를 위해 새 파일이 이미 존재하는지 확인합니다.
                if not os.path.exists(new_file):
                    os.rename(old_file, new_file)
                    print(f'Renamed file: {old_file} -> {new_file}')
                else:
                    print(f'File already exists: {new_file}')

        # 디렉토리 이름 변경
        for dirname in dirnames:
            if " " in dirname:
                new_dirname = dirname.replace(" ", "_")
                old_dir = os.path.join(dirpath, dirname)
                new_dir = os.path.join(dirpath, new_dirname)
                if not os.path.exists(new_dir):
                    os.rename(old_dir, new_dir)
                    print(f'Renamed directory: {old_dir} -> {new_dir}')
                else:
                    print(f'Directory already exists: {new_dir}')

if __name__ == "__main__":
    # 스크립트가 위치한 폴더 기준으로 root_directory를 설정합니다.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print("작업 시작 폴더:", current_dir)
    replace_space_with_underscore(current_dir)
