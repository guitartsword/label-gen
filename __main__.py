from multiprocessing import Pool

from app.load_products import get_product_label_text
from app.create_label import create_image



with Pool() as pool:
    texts = get_product_label_text()
    pool.starmap(create_image, texts)
