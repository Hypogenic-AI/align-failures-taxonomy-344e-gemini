import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('figures', exist_ok=True)

df = pd.read_csv('results/experiment_results.csv')

# Calculate percentages for boolean columns
df['omission_pct'] = df['omission'].astype(int) * 100
df['overclaiming_pct'] = df['overclaiming'].astype(int) * 100
df['metric_gaming_pct'] = df['metric_gaming'].astype(int) * 100

summary = df.groupby('condition').agg({
    'omission_pct': 'mean',
    'overclaiming_pct': 'mean',
    'metric_gaming_pct': 'mean',
    'severity': 'mean'
}).reset_index()

# Rename conditions for plotting
summary['condition'] = summary['condition'].str.replace('_', ' ')

# Set style
sns.set_theme(style="whitegrid")

# Plot 1: Failure Rates
plt.figure(figsize=(10, 6))
bar_width = 0.25
x = range(len(summary))

plt.bar([i - bar_width for i in x], summary['omission_pct'], width=bar_width, label='Omission of Negative Findings')
plt.bar(x, summary['overclaiming_pct'], width=bar_width, label='Overclaiming Results')
plt.bar([i + bar_width for i in x], summary['metric_gaming_pct'], width=bar_width, label='Metric Gaming')

plt.xlabel('Prompt Condition', fontsize=12)
plt.ylabel('Failure Rate (%)', fontsize=12)
plt.title('Alignment Failure Rates by Pressure Condition in AI-Driven Research', fontsize=14)
plt.xticks(x, summary['condition'])
plt.legend()
plt.tight_layout()
plt.savefig('figures/failure_rates.png', dpi=300)
plt.close()

# Plot 2: Severity Score
plt.figure(figsize=(8, 6))
sns.barplot(x='condition', y='severity', data=df.replace({'condition': {'Acceptance_Pressure': 'Acceptance Pressure', 'Impact_Pressure': 'Impact Pressure'}}), capsize=.1, errorbar='sd', palette='viridis')
plt.xlabel('Prompt Condition', fontsize=12)
plt.ylabel('Severity Score (1-5)', fontsize=12)
plt.title('Severity of Alignment Failures by Condition', fontsize=14)
plt.ylim(1, 5)
plt.tight_layout()
plt.savefig('figures/severity_scores.png', dpi=300)
plt.close()

print("Visualizations saved to figures/ directory.")
