from pyspark.sql import SparkSession


def get_products_with_categories(spark: SparkSession, products_df, categories_df):    
    # Использую аргумент how="left", чтобы продукты без категории попали в итоговый датафрейм
    result_df = products_df.join(categories_df, on="product_id", how="left").select("product_name", "category_name")

    return result_df


# Для примера создал два датафрейма
products = [
    (1, "MacBook Pro"),
    (2, "Dell XPS"),
    (3, "iPhone 12"),
    (4, "Apple Watch"),
    (5, "Samsung Galaxy S21"),
    (6, "Sony WH-1000XM4"),
    (7, "Amazon Echo Dot"),
    (8, "Nvidia RTX 3080"),
    (9, "Google Pixel Stand")
]
products_df = spark.createDataFrame(products, ["product_id", "product_name"])

categories = [
    (1, "Laptops"),
    (1, "Apple Products"),
    (2, "Laptops"),
    (3, "Smartphones"),
    (3, "Apple Products"),
    (4, "Smart Wearables"),
    (4, "Apple Products"),
    (5, "Smartphones"),
    (6, "Audio"),
    (6, "Headphones"),
    (7, "Smart Home Devices"),
    (8, "Graphics Cards"),
    (8, "Computer Components")
]    
categories_df = spark.createDataFrame(categories, ["product_id", "category_name"])

spark = SparkSession.builder.appName("ProductsAndCategories").getOrCreate()

result = get_products_with_categories(spark, products_df,categories_df)

# Для удобного просмотра группирую по категориям
group_by_category_df = result.groupBy("category_name").agg(F.collect_list("product_name").alias("products"))
group_by_category_df.show(truncate=False)

# Или по названиям
group_by_name_df = result.groupBy("product_name").agg(F.collect_list("category_name").alias("category"))
group_by_name_df.show(truncate=False)

# Для записи в файл использую метод write
# group_by_name_df.write.parquet("group_by_name_df.parquet")
# group_by_category_df.write.parquet("group_by_category_df.parquet")
