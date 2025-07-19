# الملف: caesar_cipher.py

# هذه الدالة هي القلب النابض للبرنامج، تقوم بتشفير أو فك تشفير النص.
def caesar_cipher(text, shift, mode='encrypt'):
    """
    يقوم بتشفير أو فك تشفير النص باستخدام خوارزمية قيصر.

    المعاملات (Parameters):
    text (str): النص المراد تشفيره أو فك تشفيره.
    shift (int): قيمة الإزاحة (عدد صحيح).
    mode (str): وضع العملية، 'encrypt' للتشفير، 'decrypt' لفك التشفير.
                القيمة الافتراضية هي 'encrypt'.

    الناتج (Returns):
    str: النص الناتج بعد التشفير أو فك التشفير.
    """
    result = "" # متغير لتخزين النص الناتج (المشفر أو المفكك)

    # إذا كان الوضع هو 'decrypt' (فك التشفير)، نعكس قيمة الإزاحة.
    # لأن فك التشفير هو عكس عملية التشفير.
    if mode == 'decrypt':
        shift = -shift

    # نمر على كل حرف في النص المدخل
    for char in text:
        # 1. التعامل مع الحروف الإنجليزية الصغيرة (a-z)
        if 'a' <= char <= 'z':
            start = ord('a') # ASCII قيمة الحرف 'a' (97)
            # نحول الحرف إلى رقم (0-25)، نضيف الإزاحة، نطبق عملية باقي القسمة 26
            # (لضمان أن الرقم يظل ضمن نطاق الحروف الأبجدية)، ثم نحوله مرة أخرى إلى حرف.
            result += chr((ord(char) - start + shift) % 26 + start)
        # 2. التعامل مع الحروف الإنجليزية الكبيرة (A-Z)
        elif 'A' <= char <= 'Z':
            start = ord('A') # ASCII قيمة الحرف 'A' (65)
            # نفس المنطق المستخدم للحروف الصغيرة، ولكن باستخدام ASCII قيمة الحرف 'A'.
            result += chr((ord(char) - start + shift) % 26 + start)
        # 3. التعامل مع الأرقام (0-9)
        elif '0' <= char <= '9':
            start = ord('0') # ASCII قيمة الرقم '0' (48)
            # نفس المنطق، لكن نطاق الأرقام هو 10 (0-9).
            result += chr((ord(char) - start + shift) % 10 + start)
        # 4. التعامل مع أي حروف أخرى (مسافات، علامات ترقيم، إلخ.)
        else:
            # أي حرف ليس حرفاً إنجليزياً (صغيراً أو كبيراً) أو رقماً، نتركه كما هو.
            result += char
    return result # نرجع النص الناتج

# هذه الدالة هي نقطة الدخول الرئيسية للبرنامج، وهي التي تتفاعل مع المستخدم.
def main():
    """
    الدالة الرئيسية لتشغيل تطبيق تشفير و فك تشفير قيصر التفاعلي.
    تتعامل مع مدخلات المستخدم وتعرض النتائج.
    """
    print("--- Caesar Cipher Application ---") 

    while True: # حلقة لا نهائية لاستمرار تشغيل التطبيق حتى يختار المستخدم الخروج
        print("\nChoose an operation:") 
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice (number): ") 

        # إذا اختار المستخدم 1 (تشفير) أو 2 (فك تشفير)
        if choice == '1' or choice == '2':
            message = input("Enter your message: ") 
            try:
                shift = int(input("Enter the shift value (integer): ")) 
            except ValueError:
                # إذا أدخل المستخدم شيئاً غير رقم للإزاحة، نظهر رسالة خطأ ونعود لبداية الحلقة.
                print("Invalid shift value. Please enter an integer.") 
                continue # نعود لبداية حلقة while

            # ننفذ عملية التشفير إذا كان الاختيار '1'
            if choice == '1':
                encrypted_message = caesar_cipher(message, shift, 'encrypt')
                print(f"Encrypted message: {encrypted_message}") 
            # ننفذ عملية فك التشفير إذا كان الاختيار '2'
            else: # choice == '2'
                decrypted_message = caesar_cipher(message, shift, 'decrypt')
                print(f"Decrypted message: {decrypted_message}")
        # إذا اختار المستخدم 3 (خروج)
        elif choice == '3':
            print("Thank you for using the application. Goodbye!") 
            break # نكسر الحلقة اللانهائية، وبالتالي ينتهي البرنامج.
        # إذا أدخل المستخدم اختياراً غير صحيح (ليس 1، 2، أو 3)
        else:
            print("Invalid choice. Please try again.") 

# هذا الشرط يضمن أن دالة 'main()' يتم استدعاؤها فقط عندما يتم تشغيل الملف مباشرة،
# وليس عندما يتم استيراد هذا الملف كوحدة (module) في ملف بايثون آخر.
if __name__ == "__main__":
    main()
