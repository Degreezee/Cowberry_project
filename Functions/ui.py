from Classes.Class_Encrypted_Image import EncryptedImage
from Classes.Class_String import String
from PIL import Image as IMG


def coding(text_to_code, label_to_ans):
    String(str(text_to_code)).str_to_full_img().image.save("image.png")

    label_to_ans.setText("Изображение сохранено в директорию приложения")


def decoding(img_path, decoded_text_box):
    image = IMG.open(str(img_path))
    decoded_image = EncryptedImage(image).decode()
    decoded_text_box.setText(decoded_image)


def clear(input1, input2, input3, input4):
    input1.setText("")
    input2.setText("")
    input3.setText("")
    input4.setText("")