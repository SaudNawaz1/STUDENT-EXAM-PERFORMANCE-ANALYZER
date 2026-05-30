# Student Exam Performance Analyzer
# Created by Saud Nawaz

import pandas as pd

# Your FSC marks data
data = {
    'Subject': [
        'English', 'Urdu', 'Mutala-e-Quran', 'Islamic Education',
        'Pakistan Studies', 'Mathematics', 'Physics', 'Computer Science'
    ],
    'Total Marks': [200, 200, 100, 50, 50, 200, 200, 200],
    'Marks Obtained': [158, 164, 97, 48, 43, 148, 127, 175]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate percentages
df['Percentage'] = (df['Marks Obtained'] / df['Total Marks']) * 100

# Analysis
average_percentage = df['Percentage'].mean()
best_subject = df.loc[df['Percentage'].idxmax(), 'Subject']
weakest_subject = df.loc[df['Percentage'].idxmin(), 'Subject']
total_marks = df['Marks Obtained'].sum()
total_possible = df['Total Marks'].sum()
overall_percentage = (total_marks / total_possible) * 100

# Print Results
print("=" * 50)
print("STUDENT EXAM PERFORMANCE ANALYZER")
print("=" * 50)

print(f"\nOverall Percentage: {overall_percentage:.2f}%")
print(f"Best Subject: {best_subject}")
print(f"Weakest Subject: {weakest_subject}")

print("\nSubject-wise Performance:")
for i, row in df.iterrows():
    print(f"{row['Subject']}: {row['Percentage']:.1f}%")

# Recommendations
print("\n" + "=" * 50)
print("RECOMMENDATIONS:")

if overall_percentage >= 80:
    print("Excellent! Focus on maintaining consistency.")

if df[df['Percentage'] < 60].shape[0] > 0:
    print("Need improvement in: " + ", ".join(df[df['Percentage'] < 60]['Subject'].values))
    print("Tip: Spend 2 extra hours weekly on your weakest subject.")

print("=" * 50)
