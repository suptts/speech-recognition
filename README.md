# speech-recognition

### Set up development environment for python programming
### Step 1: สร้าง python virtual environment
ปัญหาที่เจอสำหรับ open-source เมื่อมี version ใหม่ๆบอกมาแล้วเราใช้ในการ develop environment จะทำให้ไม่ support พวก library เก่าๆ
ดังนั้นวิธีปัองกันที่ดีที่สุดคือ freezed version ของ python และ libray ที่เราใช้

วิธีการคือสร้างไฟล์   
* 1. Setup python virtual environmentเพืื่อใช้ python specific version เช่น python 3.8, python 3.9 เป็นต้น
* 2. Freeze version ของ library ที่ใช่ก่อนนำไป deploy บน production เสมอโดยใช้ requirements.txt ช่วย
* สร้าง code (.py) มาเพื่อทดสอบว่า environment พร้อมใช้งานสำหรับ python development project เรา

### Step 2: สร้าง scaffold
ทำตามขั้นตอนใน step 1
* `requirements.txt` เป็น list of packages ที่จะใช้ใน project
* `Makefile`		เป็น cookbook ที่ไว้รัน command
* `app.py`		เป็น code ของเรา

เมื่อเสร็จแล้ว install และ ทดสอบการทำงานว่า devlepment environment พร้อมใช้งานแล้ว
* ให้เรารัน `make all` เพื่อติดตั้ง required libraies และ ทดสอบ python development tools e.g. pytest, lint, format เป็นต้น
