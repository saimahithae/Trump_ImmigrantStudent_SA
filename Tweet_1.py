import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Load your CSV file
file_path = 'Tweets_data_latest.csv'  # Adjust the file path as needed
tweets_df = pd.read_csv(file_path)

# Define a function to calculate sentiment polarity, handling non-string values
def analyze_sentiment(text):
    if not isinstance(text, str):  # Check if the text is not a string
        text = ""  # Convert non-string values to an empty string
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return polarity

# Apply sentiment analysis to the 'Tweet Content' column and create a new 'Sentiment' column
tweets_df['Sentiment'] = tweets_df['Content'].apply(analyze_sentiment)

# Categorize the sentiment as Positive, Neutral, or Negative
def categorize_sentiment(polarity):
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

tweets_df['Sentiment Category'] = tweets_df['Sentiment'].apply(categorize_sentiment)

# Ensure 'Date' is in datetime format and clean it
tweets_df['Date'] = pd.to_datetime(tweets_df['Date'], errors='coerce')  # Handle errors as NaT

# Ensure the 'Sentiment' column is numeric (if any non-numeric values exist, they will be coerced to NaN)
tweets_df['Sentiment'] = pd.to_numeric(tweets_df['Sentiment'], errors='coerce')

# Group by month and calculate the average sentiment
sentiment_trend = tweets_df.groupby(tweets_df['Date'].dt.to_period('M'))['Sentiment'].mean().reset_index()

# Drop rows with NaN values
sentiment_trend = sentiment_trend.dropna(subset=['Sentiment'])

# Ensure that 'Date' is in a compatible format for plotting
sentiment_trend['Date'] = sentiment_trend['Date'].astype(str)  # Convert PeriodIndex to string for plotting

# Plot sentiment trend over time
sns.lineplot(data=sentiment_trend, x='Date', y='Sentiment')
plt.title("Sentiment Trend Over Time")
plt.xlabel("Time (by Month)")
plt.ylabel("Sentiment Score")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# Save the result to a new CSV file
output_path = 'Tweets_with_Sentiment.csv'
tweets_df.to_csv(output_path, index=False)

print(f"Sentiment analysis complete! Results saved to {output_path}")


# Count the occurrences of each sentiment category
sentiment_counts = tweets_df['Sentiment Category'].value_counts()

# Pie chart for sentiment distribution
plt.figure(figsize=(6, 6))
sentiment_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#ff6666', '#99ff99'])
plt.title("Sentiment Distribution")
plt.ylabel('')  # Hide the y-label
plt.show()

# Bar plot for sentiment distribution
plt.figure(figsize=(6, 4))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='viridis')
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()


# Calculate a 3-month moving average for sentiment trend
sentiment_trend['Sentiment MA'] = sentiment_trend['Sentiment'].rolling(window=3).mean()

# Plot sentiment trend with moving average
plt.figure(figsize=(10, 6))
sns.lineplot(data=sentiment_trend, x='Date', y='Sentiment', label='Sentiment')
sns.lineplot(data=sentiment_trend, x='Date', y='Sentiment MA', label='3-Month Moving Average', linestyle='--', color='red')
plt.title("Sentiment Trend Over Time with Moving Average")
plt.xlabel("Time (by Month)")
plt.ylabel("Sentiment Score")
plt.xticks(rotation=45)
plt.legend()
plt.show()



# Sort by sentiment to get top positive and negative tweets
top_positive_tweets = tweets_df.sort_values(by='Sentiment', ascending=False).head(5)
top_negative_tweets = tweets_df.sort_values(by='Sentiment', ascending=True).head(5)

# Display top positive tweets
print("Top Positive Tweets:")
print(top_positive_tweets[['Content', 'Sentiment']])

# Display top negative tweets
print("Top Negative Tweets:")
print(top_negative_tweets[['Content', 'Sentiment']])


# Add a column for day of the week (0=Monday, 6=Sunday)
tweets_df['Day of Week'] = tweets_df['Date'].dt.dayofweek

# Pivot the DataFrame to get a matrix of sentiment by day and month
heatmap_data = tweets_df.pivot_table(index='Day of Week', columns=tweets_df['Date'].dt.to_period('M'), values='Sentiment', aggfunc='mean')

# Plot heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt=".2f", linewidths=.5)
plt.title("Heatmap of Sentiment by Day of Week and Month")
plt.xlabel("Month")
plt.ylabel("Day of Week")
plt.show()
