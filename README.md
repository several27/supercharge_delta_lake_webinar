## Pipelines

### demo_day

The **Demo Day** Spark pipeline is designed to showcase the capabilities of Prophecy's data processing and analysis tools. It leverages customer and order data to generate insights on customer spending patterns. The pipeline includes data transformation and enrichment steps, as well as the creation of a final table for analysis. Running the pipeline via Python in a Spark environment provides a powerful platform for data exploration and visualization.

### cleanup_orders

The **Cleanup Orders** Spark pipeline is designed to clean and transform raw order data, ensuring data quality and consistency. The pipeline leverages Python in a Spark environment to efficiently process large datasets. By running this pipeline, businesses can improve their data-driven decision-making and gain valuable insights into their operations.

### mrr_reporting

The **MRR Reporting** Spark pipeline generates a monthly recurring revenue report for a business. It extracts data from customer and order records, calculates the total revenue per customer, and enriches the report with additional customer information. Running the pipeline via Python in a Spark environment provides accurate and actionable insights for businesses to optimize their revenue streams.

### cleanup_customers

The **Cleanup Customers** Spark pipeline is designed to clean and transform customer data, ensuring data quality and consistency. The pipeline leverages Python in a Spark environment to efficiently process large datasets. By standardizing and enriching customer data, businesses can improve decision-making and enhance customer experiences.

### ingest_customers

The **Ingest Customers** Spark pipeline is responsible for extracting and transforming raw customer data into a format that can be used for analysis. The pipeline utilizes various UDFs and configuration settings to ensure data quality and consistency. Running the pipeline via Python in a Spark environment provides businesses with a reliable and scalable solution for managing customer data.

## Datasets

1. **department_table**
This dataset contains information about customers and their orders, including customer keys, names, addresses, nation keys, phone numbers, account balances, market segments, and comments. It also includes order keys, order statuses, total prices, order dates, order priorities, clerks, ship priorities, and comments. The format of this dataset is not specified, but it can be used for various data analysis tasks, such as identifying customer preferences, tracking order fulfillment, and evaluating sales performance.

2. **bronze_orders**
This dataset represents a collection of bronze orders, with each order containing a unique order key, customer key, order status, total price, order date, order priority, clerk name, shipping priority, and a comment. The absence of a specified format suggests that this dataset may be stored in a variety of formats, including but not limited to CSV, JSON, or Parquet. This dataset is valuable for analyzing customer orders, tracking sales trends, and identifying areas for improvement in the ordering process.

3. **bronze_customers**
This dataset contains information about bronze-level customers, including their unique customer keys, names, addresses, nation keys, phone numbers, account balances, market segments, and comments. The absence of a specified format suggests that this dataset may be stored in a variety of formats, such as a database or a spreadsheet. This data is useful for analyzing customer behavior, identifying trends, and making informed business decisions based on customer characteristics and preferences.

4. **silver_customers**
This dataset contains information about silver customers, including their unique customer keys, names, addresses, nation keys, phone numbers, account balances, market segments, and comments. The data is not in any specific format and can be used for various analytical purposes, such as customer segmentation, market analysis, and performance evaluation. It provides valuable insights into customer behavior and preferences, enabling businesses to make informed decisions and improve their overall performance.

## Jobs

1. **Monthly Job Airflow**

The **Monthly Job Airflow** is a recurring task that runs on the cloud compute platform. This job is designed to automate and streamline various processes, ensuring that they are executed on a monthly basis. By leveraging the power of Airflow, we can easily manage and monitor this job, ensuring that it runs smoothly and efficiently. This job helps us to maintain consistency and accuracy in our operations, contributing to improved productivity and better decision-making.

2. **Monthly Job DB**

The **Monthly Job DB** is another recurring task that runs on the cloud compute platform. This job is responsible for performing various database-related tasks on a monthly basis. By executing this job, we ensure that our databases remain up-to-date and optimized, contributing to improved performance and reliability. This job helps us to maintain the integrity of our data, ensuring that it is accurate and accessible when we need it.

*** Release notes for version: 79.0 ***

Latest release