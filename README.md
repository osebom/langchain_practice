This Python script uses LangChain and multiple open-source LLMs to categorize and summarize bank statement data. The script reads a bank statement in CSV format, categorizes each transaction into predefined categories, and then sums the transactions by category. The output is a summary of total spending by category and also a Python script (stored in google_solution.py) that hard-codes this data into an 'items' dictionary, with the category name and value and writes a Python script to sum this data by 'Category' and prints the results. This is done by parsing a PROMPT and CODING templates (one for the categorization and the other to write a Python script for the categorical sums) into a sequential chain using Prompt Templates then running both chains together. 

![image](https://github.com/osebom/langchain_practice/assets/40761922/0d46929f-ceda-42e2-9e28-b9564df4e534)

Below is a sample of the results:

<img width="358" alt="image" src="https://github.com/osebom/langchain_practice/assets/40761922/556d982d-da76-4791-bf6e-31e631e225ce">
<img width="790" alt="image" src="https://github.com/osebom/langchain_practice/assets/40761922/dfb28fe9-6375-49ff-a848-3554b0f359b6">

Great explaination of Sequential Chains in Langchain: https://www.analyticsvidhya.com/blog/2023/10/a-comprehensive-guide-to-using-chains-in-langchain/
