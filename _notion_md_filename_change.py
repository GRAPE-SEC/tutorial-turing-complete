import os
import re

# 현재 폴더의 모든 파일을 순회합니다.
for filename in os.listdir('.'):
    # 확장자가 .md 인 파일만 처리합니다.
    if filename.endswith('.md'):
        newname = filename

        # 파일명에서 뒤에 붙은 공백과 32자리 16진수 패턴 제거
        # (?=\.md$)는 확장자 .md 직전에 있는 경우만 제거합니다.
        newname = re.sub(r'\s+[0-9a-fA-F]{32}(?=\.md$)', '', newname)

        # 파일명 내 모든 공백을 언더스코어로 변경
        newname = newname.replace(' ', '_')

        # 파일명이 변경되었으면 파일 이름을 변경합니다.
        if newname != filename:
            os.rename(filename, newname)
            print(f"Renamed '{filename}' -> '{newname}'")
