from PIL import Image
from reportlab.pdfgen import canvas
import os
import sys

def convert_image_to_pdf(image_path, output_pdf):
    # אם התמונה היא תיקייה ולא קובץ בודד
    if os.path.isdir(image_path):
        files = [f for f in os.listdir(image_path) if f.endswith(('jpg', 'jpeg', 'png'))]
        files.sort()  # מיון קבצים לפי שם
    else:
        files = [image_path]

    c = canvas.Canvas(output_pdf)
    y_position = 800  # מיקום התחלה בגובה

    for image_file in files:
        full_image_path = os.path.join(image_path, image_file) if os.path.isdir(image_path) else image_path
        img = Image.open(full_image_path)
        c.drawImage(full_image_path, 100, y_position, width=400, height=300)
        y_position -= 350  # ירידה בגובה בין התמונות
        if y_position < 100:
            c.showPage()  # מעבר לדף חדש אם יש צורך

    c.save()

if __name__ == "__main__":
    # לוודא שהוזן נתיב תמונה
    if len(sys.argv) < 2:
        print("Usage: python convert_image_to_pdf.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    output_pdf = "output/converted_output.pdf"  # תיקיית output לשמירת ה-PDF

    convert_image_to_pdf(image_path, output_pdf)
    print(f"PDF saved as {output_pdf}")

