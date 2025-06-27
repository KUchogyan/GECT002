# It's a subfile of week12.

# 1. 다운로드할 동영상 주소 가져오기
# 2. 동영상에 대한 정보(타이틀, 자막, 화질 등) 선택
# 3. 선택한 동영상을 다운로드

from pytubefix import YouTube

url = input("다운로드할 유튜브 주소를 입력해 주세요 >> ")
vi = YouTube(url)
selected_video = vi.streams.get_highest_resolution()
print(f"Downloading {selected_video.title()}")
print(">> 다운로드 중입니다...")
selected_video.download()
print("다운로드가 완료되었습니다.")
