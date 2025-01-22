import os
import pandas as pd
import numpy as np
from django.db import IntegrityError
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
        try:
            # جلوگیری از ایجاد داده‌های تکراری برای Division
            division, _ = Division.objects.get_or_create(name=row.get('Division Name', 'Unknown Division'))
            
            # جلوگیری از ایجاد داده‌های تکراری برای Department
            department, _ = Department.objects.get_or_create(name=row.get('Department Name', 'Unknown Department'))
            
            # جلوگیری از ایجاد داده‌های تکراری برای ProductClass
            product_class, _ = ProductClass.objects.get_or_create(name=row.get("Class Name", 'Unknown Class'))
            
            # مدیریت مقادیر ناقص برای Review
            title = row["title"]
            content = row["Review Text"]
            rating = row["Rating"]
            
            # اگر امتیاز مشخص نباشد، مقدار پیش‌فرض داده می‌شود
            if not rating or not isinstance(rating, int) or rating < 1 or rating > 5:
                rating = 3  # مقدار پیش‌فرض
            
            # ایجاد و ذخیره یک نظر
            review = Review.objects.create(
                title=title,
                content=content,
                rating=rating,
                division=division,
                department=department,
                product_class=product_class
            )
            
            print(f"Review for '{title}' saved successfully.")

        except IntegrityError as e:
            print(f"IntegrityError: {e} - Skipping row.")
            continue
        
        except Exception as e:
            print(f"Error processing row: {e} - Skipping row.")
            continue

        review.save(using='default')
    print("df_part1 ont été sauvegardées dans sqlite3 avec succès !")
    
    
 
            
    for _, row in df_part2.iterrows(): 
        try:
            # جلوگیری از ایجاد داده‌های تکراری برای Division
            division, _ = Division.objects.get_or_create(name=row.get('Division Name', 'Unknown Division'))
            
            # جلوگیری از ایجاد داده‌های تکراری برای Department
            department, _ = Department.objects.get_or_create(name=row.get('Department Name', 'Unknown Department'))
            
            # جلوگیری از ایجاد داده‌های تکراری برای ProductClass
            product_class, _ = ProductClass.objects.get_or_create(name=row.get("Class Name", 'Unknown Class'))
            
            # مدیریت مقادیر ناقص برای Review
            title = row["title"]
            content = row["Review Text"]
            rating = row["Rating"]
            
            # اگر امتیاز مشخص نباشد، مقدار پیش‌فرض داده می‌شود
            if not rating or not isinstance(rating, int) or rating < 1 or rating > 5:
                rating = 3  # مقدار پیش‌فرض
            # ایجاد و ذخیره یک نظر
            review = Review.objects.create(
                title=title,
                content=content,
                rating=rating,
                division=division,
                department=department,
                product_class=product_class
            )
            
            print(f"Review for '{title}' saved successfully.")

        except IntegrityError as e:
            print(f"IntegrityError: {e} - Skipping row.")
            continue
        
        except Exception as e:
            print(f"Error processing row: {e} - Skipping row.")
            continue
        
        review.save(using='mysql_db')
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
         
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
