import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate synthetic data
data = {
    "Product Category": ["Electronics", "Clothing", "Home & Kitchen", "Beauty", "Sports", "Toys"],
    "Satisfaction Score": [4.2, 3.8, 4.5, 3.6, 4.1, 3.9]
}
df = pd.DataFrame(data)

# Set professional style
sns.set_style("whitegrid")
sns.set_context("talk")

# Create figure with correct size for 512x512
plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512px

# Barplot
sns.barplot(x="Product Category", y="Satisfaction Score", data=df, hue="Product Category", palette="viridis", legend=False)


# Labels and Title
plt.title("Average Customer Satisfaction by Product Category", fontsize=16, weight="bold")
plt.xlabel("Product Category", fontsize=12)
plt.ylabel("Satisfaction Score (out of 5)", fontsize=12)
plt.xticks(rotation=20)

# Save chart exactly 512x512
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
