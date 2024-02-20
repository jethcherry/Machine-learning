import csv
import random

# Define the factors that affect business growth
factors = [
    "Revenue (Shillings)", "Profit (Shillings)", "Loss (Shillings)",
    "Customer Acquisition Cost (Shillings)", "Customer Lifetime Value (Shillings)",
    "Market Share (Percentage)", "Customer Satisfaction (Percentage)",
    "Employee Satisfaction (Percentage)", "Product Quality (Rating out of 10)",
    "Innovation (Rating out of 10)", "Market Trends (Rating out of 10)",
    "Type of Business", "Business Size", "Geographic Location",
    "Industry Trends (Percentage)", "Business Reputation (Percentage)",
    "Customer Retention Rate (Percentage)", "Employee Turnover Rate (Percentage)",
    "Market Saturation (Percentage)", "Pricing Strategy (Rating out of 10)",
    "Cost Management (Rating out of 10)", "Legal and Regulatory Compliance (Percentage)",
    "Brand Awareness (Percentage)", "Distribution Channels", "Customer Demographics",
    "Market Entry Barriers (Rating out of 10)", "Technological Disruption (Rating out of 10)",
    "Intellectual Property Protection (Percentage)", "Market Positioning (Percentage)",
    "Seasonal Variations (Percentage)", "Economic Indicators (Percentage)",
    "Partnerships and Alliances", "Quality of Leadership (Rating out of 10)",
    "Employee Morale (Rating out of 10)", "Financial Stability (Percentage)",
    "Customer Loyalty Programs (Percentage)", "Online Presence and E-commerce Strategy (Percentage)",
    "External Economic Factors (Percentage)",
    "Target"  # Add target as a factor
]

# Generate random data for each factor
dataset = []
for _ in range(30000):  # Number of rows in the dataset
    row = {factor: random.uniform(0, 50000) if "Shillings" in factor else random.uniform(0, 10) if "Rating" in factor else random.uniform(0, 100) for factor in factors[:-1]}
    row['Type of Business'] = random.choice(["Manufacturing","E-commerce",
                                             "Consulting","Education","Real Estate",
                                             "Transportation","Food and Beverage","Entertainment","Construction"
                                             ,"Agriculture","Energy","Media","Fashion","Fitness and Wellness","Automotive","Tourism and Travel",
                                             "Legal_Services","Event Planning","Environmental Services","Software Development","Marketing and Advertising"
                                             ,"Nonprofit/NGOGovernment/Public Sector","Pharmaceuticals","Telecommunications"])
    
    row['Business Size'] = random.choice(["Small", "Medium", "Large"])
    row['Geographic Location'] = random.choice(["Urban", "Suburban", "Rural"])
    row['Distribution Channels'] = random.choice(["Online", "Offline", "Both"])
    row['Customer Demographics'] = random.choice(["Youth", "Adults", "Seniors", "Mixed"])
    row['Partnerships and Alliances'] = random.choice(["Yes", "No"])
    
    # Convert 'Yes'/'No' to integer (1/0)
    row['Partnerships and Alliances'] = 1 if row['Partnerships and Alliances'] == 'Yes' else 0
    
    # Bias the selection towards '1' (growth) by setting a probability
    row['Target'] = random.choices([0, 1], weights=[0.2, 0.8])[0]  # Adjust weights as needed
    
    dataset.append(row)

# Write the dataset to a CSV file
csv_file = "business_growth_dataset.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=factors)
    writer.writeheader()
    writer.writerows(dataset)

print(f"Dataset has been saved to {csv_file}")
