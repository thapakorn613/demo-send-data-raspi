1. แตกไฟล์ python-firebase.rar
2. สามารถรัน script "python demo-test-send.py"
    - มันจะส่ง ข้อความ string จากตัวแปร msg_name ไปที่ firebase 
    - และส่ง ข้อความ string จากตัวแปร msg_text ไปที่ firebase 
    โดยมีการอ้างจาก classes "aarApi"
    สามารถส่งได้เป็นแบบอื่นๆ NAME.sendMessage("art","5")
    *** ซึ่งหากน้องจะเอาไปใช้ในโปรเจคน้อง พี่แนะนำว่า ให้ import classes เข้ามาแบบ
    ในตัวอย่างไฟล์นี้ 
    และถ้า python ของน้องมีการเช็คเจอหน้าก็ให้ใส่ if-else ประมาณนี้ 
    if ( vareDetectFace == 5):
        protocol = aar.aarApi()
        // โดยที่ YOUR_NAME เป็นชื่อของคนที่ถูกโปรแกรมน้องจำใบหน้า 
        protocol.sendMessage( YOUR_NAME ,msg_text)
        // เช่น YOUR_NAME = "art"
        YOUR_NAME = getName()
        protocol.sendMessage( YOUR_NAME ,msg_text)



