import subprocess
import json
import random

# ตั้งค่า Twitch CLI command และข้อมูลการให้ OAuth Token
twitch_cli_command = 'curl -X GET "https://api.twitch.tv/helix/chat/chatters?broadcaster_id=626342428&moderator_id=22489982" -H "Authorization: Bearer bc2fgncb9sq2c5sdlq5x0wdoiy3wkp" -H "Client-Id: 8kdh03pq2h0cs41lz6l85pqizwwzeu"'

# ใช้ subprocess เพื่อเรียกใช้คำสั่ง CLI และดึงผลลัพธ์
result = subprocess.run(twitch_cli_command, capture_output=True, text=True, shell=True)

# ตรวจสอบว่าคำสั่งทำงานสมบูรณ์หรือไม่
if result.returncode == 0:
    # แปลง JSON response เป็น Python dictionary
    twitch_cli_response = json.loads(result.stdout)

    # ดึงข้อมูล user_name ทั้งหมด
    viewers = [viewer['user_login'] for viewer in twitch_cli_response['data']]

    # สุ่ม user_name
    random_viewer_name = random.choice(viewers)

    print(f'{random_viewer_name}')
else:
    print('Error executing Twitch CLI command')
    print(result.stderr)
