# Example usage
from app.load_products import get_product_label_text
from app.create_label import create_image


texts = get_product_label_text()
for text in texts:
    t1, t2 = text.split('\n')
    create_image(t1, t2)
    print('done >>>', t1)