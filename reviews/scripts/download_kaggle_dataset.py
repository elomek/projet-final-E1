import os
import pandas as pd
import numpy as np
from config.settings import DATABASES

from reviews.models import Review, Department, Division, ProductClass




def download_kaggle_dataset():
    os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
    os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')
    #kaggle datasets download -d nicapotato/womens-ecommerce-clothing-reviews --unzip -p /Users/elhamkaramian/Desktop/final_project_E1
    #ا  با استفاده از دستور بالا در ترمینال فایل زیپ را اکسترکت کردم  
    df= pd.read_csv("/code/Womens Clothing E-Commerce Reviews.csv") # mibare be mohite docker
    
    print(df.head())
    print(df.shape[0])
    #python manage.py shell
    #from reviews.scripts.download_kaggle_dataset import run  => استفاده از این سه دستور در ترمینال میشه پنج ردیف اول رو دید
    #run()
  
    
    
    # Data cleaning
    # شمارش تعداد ردیف‌هایی که مقادیر خالی دارند برای ستون‌های مشخص
    missing_rows = df[['Review Text', 'Title', 'Rating', 'Division Name', 'Department Name', 'Class Name']].isna().sum()
    print(missing_rows)
    
    df=df.dropna(subset=['Review Text'])
    df['Title']=df['Title'].fillna('Unknown')
    df['Division Name'] = df['Division Name'].fillna('Other')
    df['Department Name'] = df['Department Name'].fillna('Other')
    df['Class Name'] = df['Class Name'].fillna('Other')
    print(df.isna().sum())
    print(df.shape[0])
    
    
    
    #The dataset was divided into two equal parts  
    df_part1, df_part2 = np.array_split(df, 2)
    os.makedirs("/Users/elhamkaramian/Desktop/final_project_E1", exist_ok=True)
    df_part1.to_csv("/Users/elhamkaramian/Desktop/final_project_E1/part1.csv", index=False)
    df_part2.to_csv("/Users/elhamkaramian/Desktop/final_project_E1/part2.csv", index=False)
    print(df_part1.shape[0], 'part1')
    print(df_part2.shape[0])
    
    for _, row in df_part1.iterrows(): 
        division, _= Division.objects.get_or_create(name=row['Division Name'])
        department, _=Department.objects.get_or_create(name=row['Department Name'])
        product_class, _=ProductClass.objects.get_or_create(name=row["Class Name"])
    
        review = Review(
            title=row.get('Title', None), 
            content=row.get('Review Text', None),
            rating=row.get('Rating', 0),
            division=division,
            department=department,
            product_class=product_class
        )
        review.save(using='default')
    print("df_part1 ont été sauvegardées dans sqlite3 avec succès !")
    
    
    
    
    for _, row in df_part2.iterrows():
        division, _ = Division.objects.get_or_create(name=row['Division Name'])
        department, _ = Department.objects.get_or_create(name=row['Department Name'])
        product_class, _ = ProductClass.objects.get_or_create(name=row["Class Name"])
        
        review = Review(
            title=row.get('Title', None), 
            content=row.get('Review Text', None),
            rating=row.get('Rating', 0),
            division=division, 
            department=department, 
            product_class=product_class
        )
        try:
            review.save(using='mysql_db') 
        except Exception as e:
            print(f"خطا در ذخیره review: {e}")# ذخیره در MySQL

    print("df_part2 ont été sauvegardées dans MySQL avec succès !")
  


        
def run():
    print("Le script fonctionne !")
    download_kaggle_dataset()  
     #python manage.py shell
    #from reviews.scripts.download_kaggle_dataset import run  => استفاده از این سه دستور در ترمینال میشه پنج ردیف اول رو دید
    #run()
    
# "django_extensions"
# python manage.py makemigrations
#python manage.py migrate --database=default      
#python manage.py migrate --database=mysql_db     
         
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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