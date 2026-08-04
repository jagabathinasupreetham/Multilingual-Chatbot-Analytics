import pandas as pd
import random

# 1. Define the parameters for our fake data
num_rows = 1000
interaction_ids = range(1, num_rows + 1)
customer_ids = [random.randint(100, 999) for _ in range(num_rows)]

# Realistic categories for customer interactions
intents = ["Billing Issue", "Password Reset", "Product Inquiry", "Technical Support", "Refund Request"]
sentiments = ["Positive", "Neutral", "Negative"]
resolutions = ["Resolved", "Escalated to Human", "Pending"]

# 2. Generate the random data
data = {
    "Interaction_ID": interaction_ids,
    "Customer_ID": customer_ids,
    "Date": pd.date_range(start="2026-06-01", periods=num_rows, freq="h"),
    "Customer_Intent": [random.choice(intents) for _ in range(num_rows)],
    "Chat_Duration_Seconds": [random.randint(30, 600) for _ in range(num_rows)],
    "Customer_Sentiment": [random.choice(sentiments) for _ in range(num_rows)],
    "Resolution_Status": [random.choice(resolutions) for _ in range(num_rows)]
}

# 3. Put it into a Pandas DataFrame 
df = pd.DataFrame(data)

# 4. Export it as a clean CSV file directly into your specific Mac folder
df.to_csv("/Users/supreethamjagabathina/projects.gen ai/chatbot_interactions_1000.csv", index=False)

print("✅ Success! Your 1,000-row CSV file has been created and is ready for Tableau.")