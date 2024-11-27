import os
import pandas as pd
import numpy as np




def download_kaggle_dataset():
    os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
    os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')
#kaggle datasets download -d nicapotato/womens-ecommerce-clothing-reviews --unzip -p /Users/elhamkaramian/Desktop/final_project_E1
    #ا  با استفاده از دستور بالا در ترمینال فایل زیپ را اکسترکت کردم  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#BASE_DIR = "/code/data"     
#RAW_DATASET_PATH = os.path.join(BASE_DIR, "Womens_Clothing_E-Commerce_Reviews.csv")
#PART1_PATH = os.path.join(BASE_DIR, "part1.csv")
#PART2_PATH = os.path.join(BASE_DIR, "part2.csv")
    
    #if not os.path.exists(BASE_DIR):
        #os.makedirs(BASE_DIR)
    # دستور دانلود دیتاست
    #os.system(f"kaggle datasets download -d nicapotato/womens-ecommerce-clothing-reviews -p {BASE_DIR}")
    #os.system(f"unzip {BASE_DIR}/womens-ecommerce-clothing-reviews.zip -d {BASE_DIR}")
    #print("Dataset downloaded and extracted.")
    
#def split_and_save_dataset():
    
    #if not os.path.exists(RAW_DATASET_PATH):
        #print("Dataset not found. Please download the dataset first.")
        #return

    # خواندن فایل CSV
    #df = pd.read_csv(RAW_DATASET_PATH)

    # تقسیم داده‌ها به دو بخش
    #df_part1, df_part2 = np.array_split(df, 2)

    # ذخیره در فایل‌ها
    #df_part1.to_csv(PART1_PATH, index=False)
    #df_part2.to_csv(PART2_PATH, index=False)
    #print(f"Datasets saved: {PART1_PATH}, {PART2_PATH}")
#if __name__ == "__main__":
    #download_kaggle_dataset()
    #split_and_save_dataset()