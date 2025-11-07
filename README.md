# Sales-Forecasting-Datascience-Project
Develop a data science project using historical sales data to build a regression model that accurately predicts future sales. Preprocess the dataset, conduct exploratory analysis, select relevant features, and employ regression algorithms for model development. Evaluate model performance, optimize hyperparameters, and provide actionable insights.
## Problem Statement:
The problem is to develop a sales forecasting regression model that can accurately predict future sales based on historical sales data. This will enable businesses to make informed decisions regarding inventory management, resource allocation, and sales strategy.
## Solution Approach:
The solution approach involves utilizing machine learning techniques to analyze patterns and trends in the historical sales data. The dataset will be preprocessed to handle missing values and relevant features will be engineered. Regression algorithms such as Linear Regression, Decision Trees, Random Forests,Extra Trees or Gradient Boosting such as XGBoost, CatBoost, Light GBM will be employed to train the sales forecast model. The model's performance will be evaluated using appropriate metrics, and hyperparameter tuning will be conducted to optimize its accuracy.
## Observation:
Through exploratory data analysis, it is observed that sales exhibit seasonality and are influenced by factors such as marketing campaigns, product attributes, pricing, and external factors like economic indicators. There may also be correlation among different variables. Also every columns in the dataset is explained briefly below:
 * Item Identifier - This column gives the detailed desription about the type of the item. We can derive the nature of the item such as Food, Drink and Non-Consumables from this column.
 * Item Weight - This gives the net weight of the product.
 * Item Fat Content - This column gives the category of the fat content distributed among the products. And it is divided into two categories such as Low Fat, Regular.
 * Item Visibility - This is a measure of how prominently an item is displayed in a store. Items that are more visible are more likely to be seen by customers, and therefore more likely to be purchased.
 * Item Type - This column gives the type of the items such as Bread, Baking Goods, Breakfast, Diaries, Frozen Foods etc.
 * Item MRP - This gives the Maximum Retail Price of the product to be sold in the market.
 * Outlet Identifier - This gives the descriptive analytics about the Outlet.
 * Outlet Establishment Year - This gives the Establishment Year (i.e., Starting Year) of the Outlet.
 * Outlet Size - This gives the categories of the size of the outlets such as Medium, High and Small.
 * Outlet Location Type - It describes the location type of the Outlet being located. And it is categorized as follows : Tier 1, Tier 2 and Tier 3.
 * Outlet Type - This gives the type of the outlet based on revenue generated or investment or size of the outlet. This are further categorized as Grocery Store, SuperMarket - Type 1, Type 2, Type 3.
 * Item Outlet Sales - This gives the sales value of the item from the outlet.
## Findings :
Based on the regression model, it is found that certain product attributes, marketing natures, and pricing strategies have a significant impact on sales. The model accurately predicts future sales with a reasonable degree of accuracy, providing businesses with reliable forecasts for decision-making. The findings also highlight the importance of external factors in sales fluctuations, enabling businesses to adapt their strategies accordingly. Overall, the sales forecasting regression model proves to be a valuable tool for improving sales performance and optimizing business operations.
## Insights : 
The insights gained from the model and data analysis can provide valuable information for business decision-making. For example, the model can identify the most significant factors influencing sales performance and quantify their impact. It can also highlight the most effective marketing natures, optimal pricing strategies, and the potential impact of external factors on sales. These insights can help businesses allocate resources effectively, optimize inventory levels, outlet location and devise strategies to maximize sales. 

## Deploy to GitHub and run the Streamlit app

Follow these steps to put this project under git and push it to GitHub. The commands below are for PowerShell on Windows — replace <USERNAME> and <REPO> with your values.

1. Initialize git (if not already a git repo) and make the first commit:

	git init
	git add .
	git commit -m "Initial commit - Sales Forecasting Data Science Project"

2. Create a repository on GitHub and push (choose one):

- Using the GitHub CLI (`gh`) (recommended if installed and authenticated):

	gh repo create <USERNAME>/<REPO> --public --source=. --remote=origin --push

- Or create a repo manually on GitHub.com, then add the remote and push:

	git remote add origin https://github.com/<USERNAME>/<REPO>.git
	git branch -M main
	git push -u origin main

3. Verify the repository on GitHub: open `https://github.com/<USERNAME>/<REPO>` and confirm files are present.

4. Deploy the Streamlit app (quick options):

- Streamlit Community Cloud (recommended for quick demos):
  - Create an account at https://share.streamlit.io
  - Connect your GitHub repo and choose the branch `main` and the file `streamlit_app.py` as the app entrypoint.

- Alternatively, deploy to Heroku or other platforms by following their Python app deployment instructions.

Notes:
- `.gitignore` has been added to exclude datasets, pickles and virtual environments.
- A minimal GitHub Actions CI workflow has been added at `.github/workflows/ci.yml` which performs a smoke test. You can enable linting by adding `flake8` to `Requirements.txt` and adjusting the workflow.

