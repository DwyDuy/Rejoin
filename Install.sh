#!/bin/bash
# Tự động tải code về thư mục chính
rm -rf ~/RobloxAuto
mkdir -p ~/RobloxAuto
curl -L https://raw.githubusercontent.com/TEN_USER_CUA_BAN/RobloxAuto/main/rejoin.py -o ~/RobloxAuto/rejoin.py
echo "Đã cài đặt xong!"
