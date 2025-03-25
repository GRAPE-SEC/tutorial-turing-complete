import os
import re

def rename_folder(folder_name):
    """
    폴더명에서 뒤에 붙은 공백과 해시(16진수 문자열)를 제거하고,
    나머지 부분의 공백은 언더스코어(_)로 치환합니다.
    """
    # 폴더 이름이 "텍스트 공백 해시" 형태일 경우를 찾습니다.
    match = re.match(r"^(.*?)\s+[0-9a-fA-F]+$", folder_name)
    if match:
        base_name = match.group(1)
    else:
        base_name = folder_name
    # 공백을 언더스코어로 변경
    new_name = base_name.replace(" ", "_")
    return new_name

def rename_subfolders_in_directory(target_dir):
    # 지정한 디렉토리의 모든 항목을 순회
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        if os.path.isdir(item_path):
            new_name = rename_folder(item)
            if new_name != item:
                new_path = os.path.join(target_dir, new_name)
                print(f"Renaming '{item_path}' -> '{new_path}'")
                os.rename(item_path, new_path)

if __name__ == "__main__":
    # 현재 폴더에서 실행하거나, 원하는 폴더 경로로 변경하세요.
    target_directory = "."  
    rename_subfolders_in_directory(target_directory)
