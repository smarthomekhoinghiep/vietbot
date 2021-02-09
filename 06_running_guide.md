
### STEP1. Chạy Manual

1.1. Truy nhập vào thư mục Bot
Sử dụng lệnh sau

```sh
cd vietbot
```
1.2. Chạy boot bằng lệnh 

```sh
python3 main_process.py
```

### STEP2.  Chạy tự động khi khởi động Pi

Sử dụng lần lượt các lệnh sau

```sh
sudo apt-get install supervisor -y

```

sau khi cài đặt xong supervisor, gõ lệnh sau:

```sh
sudo nano /etc/supervisor/conf.d/bot.conf

```

Tại cửa sổ nano, gõ các dòng sau

```sh
[program:bot]
directory=/home/pi/vietbot
command=/bin/bash -c 'cd /home/pi/vietbot && python3 main_process.py'
numprocs=1
autostart=true
autorestart=true
user=pi
```
Bấm Ctrl + X, Y, Enter

Sau đó gõ tiếp các lệnh sau
```sh
sudo supervisorctl update
```
Chờ sau khi có thông báo update, khởi động lại Pi và bot sẽ tự động chạy (Chú ý thời gian chạy của bot sau khi khởi động)
