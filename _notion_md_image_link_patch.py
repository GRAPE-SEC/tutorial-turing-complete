import os
import re
import urllib.parse

def convert_md_file(file_path):
    # md 파일명에서 확장자 제거 후, 폴더명 형식으로 변환 (공백과 점을 언더스코어로)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    folder_name = base_name.replace(" ", "_").replace(".", "_")
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 정규표현식: ![alt text](url)
    def repl(match):
        alt_text = match.group(1)
        url = match.group(2)
        # URL 디코딩 후, 파일명만 추출 (마지막 경로 구성요소)
        decoded = urllib.parse.unquote(url)
        image_file = os.path.basename(decoded)
        # 이미지 파일명에서도 공백을 언더스코어로 대체
        image_file = image_file.replace(" ", "_")
        # 새 URL: /images/<폴더명>/<이미지파일>
        new_url = f"/images/{folder_name}/{image_file}"
        return f"![{alt_text}]({new_url})"
    
    new_content = re.sub(r"!\[(.*?)\]\((.*?)\)", repl, content)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Processed {file_path}")

def process_all_md_files(root_dir):
    # root_dir 및 하위 폴더의 모든 .md 파일 처리
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".md"):
                file_path = os.path.join(dirpath, filename)
                convert_md_file(file_path)

if __name__ == "__main__":
    # 스크립트가 위치한 폴더 기준으로 처리
    current_dir = os.path.dirname(os.path.abspath(__file__))
    process_all_md_files(current_dir)
