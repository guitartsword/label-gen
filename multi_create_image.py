from app.create_label import create_image

def create_image_parallel(text1, text2):
    create_image(text1, text2)
    print('done >>>', text1, flush=True)
