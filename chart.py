import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Professional styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data
df = pd.DataFrame({
    "Category": ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Books"],
    "Satisfaction": [8.2, 7.5, 8.8, 7.9, 8.4]
})

# Set figure size (8x8 inches at 64 dpi = 512x512 px)
plt.figure(figsize=(8, 8), dpi=64)

# Create Seaborn barplot
sns.barplot(
    x="Category",
    y="Satisfaction",
    data=df,
    palette="viridis"
)

# Labels and title
plt.title("Average Customer Satisfaction by Product Category", fontsize=16)
plt.xlabel("Product Category", fontsize=12)
plt.ylabel("Satisfaction Score", fontsize=12)

# Save as exactly 512x512 pixels
output_path = "/mnt/data/chart.png"
plt.savefig(output_path, dpi=64, bbox_inches="tight")
plt.close()

output_path
