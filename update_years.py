"""
연도 자동화 스크립트
app.py 파일의 하드코딩된 연도를 자동 연도 변수로 교체합니다.
"""

import re

# 파일 읽기
with open('c:/Users/USER/Desktop/TESTER_BACKUP/ComeSys_QMS-main/app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 백업 생성
with open('c:/Users/USER/Desktop/TESTER_BACKUP/ComeSys_QMS-main/app_backup.py', 'w', encoding='utf-8') as f:
    f.write(content)

# 교체 매핑
replacements = {
    # 변수명 교체 (_2023, _2024, _2025 -> _prev2, _prev1, _current)
    '_2023': '_prev2',
    '_2024': '_prev1',
    '_2025': '_current',
    
    # 문자열 내 연도 교체 ('2023', '2024', '2025' -> previous_year_2_str, previous_year_1_str, current_year_str)
    "== '2023'": "== previous_year_2_str",
    "== '2024'": "== previous_year_1_str",
    "== '2025'": "== current_year_str",
    ".contains('2025": f".contains('{{{current_year_str}}}",
}

# 특별한 패턴들 교체
# 월별 데이터 쿼리 패턴
for month in range(1, 13):
    month_str = f"{month:02d}"
    old_pattern = f"contains('2025.{month}.')"
    new_pattern = f"contains(current_year_str + '.{month}.')"
    content = content.replace(old_pattern, new_pattern)

# 기본 교체 수행
for old, new in replacements.items():
    content = content.replace(old, new)

# 파일 저장
with open('c:/Users/USER/Desktop/TESTER_BACKUP/ComeSys_QMS-main/app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("연도 자동화가 완료되었습니다!")
print("백업 파일: app_backup.py")
