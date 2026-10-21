import pandas as pd

# Load the student dataset
df = pd.read_csv("StudentsPerformance.csv")

# Display the first five rows
print(df.head())

# Display dataset dimensions
print("Dataset shape:", df.shape)

# Display column names
print("Columns:", df.columns.tolist())


# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Display data types
print("\nData Types:")
print(df.dtypes)

print("Missing values:")
print(df.isnull().sum())

print("\nZero scores:")
print((df[["math score", "reading score", "writing score"]] == 0).sum())


# 1. Calculate average marks for each subject
subjects = ["math score", "reading score", "writing score"]

print("\nAVERAGE SUBJECT SCORES")
print(df[subjects].mean().round(2))



# 2. Calculate each student's overall average
df["average score"] = df[subjects].mean(axis=1)

# 3. Display the top five performers
top_five = df.nlargest(5, "average score")

print("\nTOP FIVE PERFORMERS")
print(
    top_five[
        ["gender", "math score", "reading score",
         "writing score", "average score"]
    ].to_string(index=False)
)


import matplotlib.pyplot as plt

# Average score comparison chart
averages = df[subjects].mean()

averages.plot(kind="bar", title="Average Scores by Subject")

plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("average_scores.png")
plt.show()


import os
import matplotlib.pyplot as plt
import seaborn as sns

# Create folder to save charts
os.makedirs("visuals", exist_ok=True)

subjects = ["math score", "reading score", "writing score"]

# Chart 2: Average scores by gender
gender_scores = df.groupby("gender")[subjects].mean()

gender_scores.plot(kind="bar", figsize=(8, 5))
plt.title("Average Scores by Gender")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("visuals/gender_comparison.png")
plt.show()


# Chart 3: Effect of test preparation
prep_scores = df.groupby("test preparation course")[subjects].mean()

prep_scores.plot(kind="bar", figsize=(8, 5))
plt.title("Scores by Test Preparation Course")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("visuals/test_preparation.png")
plt.show()


# Chart 4: Parental education and student scores
parent_scores = df.groupby(
    "parental level of education"
)[subjects].mean()

parent_scores.plot(kind="bar", figsize=(10, 5))
plt.title("Scores by Parental Education")
plt.ylabel("Average Marks")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("visuals/parental_education.png")
plt.show()


# Chart 5: Distribution of maths scores
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="math score", bins=15, kde=True)
plt.title("Distribution of Maths Scores")
plt.xlabel("Maths Marks")
plt.tight_layout()
plt.savefig("visuals/math_distribution.png")
plt.show()


# Chart 6: Relationship between subject scores
plt.figure(figsize=(7, 5))
sns.heatmap(
    df[subjects].corr(),
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)
plt.title("Correlation Between Subject Scores")
plt.tight_layout()
plt.savefig("visuals/score_correlation.png")
plt.show()

print("All charts created and saved in the visuals folder!")



# PROJECT INSIGHTS

subjects = ["math score", "reading score", "writing score"]

print("\n" + "=" * 45)
print("STUDENT PERFORMANCE ANALYSIS: KEY INSIGHTS")
print("=" * 45)

# 1. Average score in each subject
averages = df[subjects].mean()
print("\n1. Average subject scores:")
print(averages.round(2))

# 2. Highest average-scoring subject
print("\n2. Highest average-scoring subject:",
      averages.idxmax(), "-", round(averages.max(), 2))

# 3. Lowest average-scoring subject
print("3. Lowest average-scoring subject:",
      averages.idxmin(), "-", round(averages.min(), 2))

# 4. Average scores by gender
print("\n4. Average scores by gender:")
print(df.groupby("gender")[subjects].mean().round(2))

# 5. Average scores by test preparation
print("\n5. Average scores by test preparation:")
print(df.groupby("test preparation course")[subjects].mean().round(2))

# 6. Average scores by lunch type
print("\n6. Average scores by lunch type:")
print(df.groupby("lunch")[subjects].mean().round(2))

# 7. Average scores by parental education
print("\n7. Average scores by parental education:")
print(df.groupby("parental level of education")[subjects].mean().round(2))

# 8. Students scoring 90 or above in maths
print("\n8. Students scoring 90+ in maths:",
      (df["math score"] >= 90).sum())

# 9. Students scoring below 40 in maths
print("9. Students scoring below 40 in maths:",
      (df["math score"] < 40).sum())

# 10. Correlation between reading and writing
correlation = df["reading score"].corr(df["writing score"])
print("10. Reading-writing score correlation:",
      round(correlation, 3))

print("\nINSIGHT GENERATION COMPLETE!")


# Save the analyzed dataset
df.to_csv("cleaned_students.csv", index=False)

print("Cleaned dataset saved successfully!")