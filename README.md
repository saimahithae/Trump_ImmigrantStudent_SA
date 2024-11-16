# Trump_ImmigrantStudent_SA

**Report on Sentiment Analysis of Tweets Regarding Trump’s Policies and Their Impact on Indian F1 Students in the U.S.**

### Project Objective
The goal of this analysis is to examine the sentiment on social media, specifically Twitter, concerning former President Donald Trump's immigration policies and their influence on Indian F1 students in the U.S. The project focuses on aspects such as student enrollment, visa issuance, job opportunities, and overall social sentiment regarding these policies.

### Data and Methodology
The analysis used a dataset of tweets with content related to Donald Trump's policies and international students. The steps taken in this analysis include:
1. **Data Cleaning**: The dataset was checked for non-string values and dates were converted to a compatible format.
2. **Sentiment Analysis**: Using TextBlob, each tweet's sentiment was analyzed and given a polarity score:
   - **Positive** for a score > 0,
   - **Neutral** for a score = 0, and
   - **Negative** for a score < 0.
3. **Sentiment Categorization**: The polarity scores were categorized as positive, neutral, or negative.
4. **Trend Analysis**: Monthly sentiment averages were calculated to track the sentiment trend over time.
5. **Visualization**: Various plots, including line plots for trends, a pie chart, and a heatmap, were generated to visualize sentiment distribution and temporal patterns.

### Key Findings

#### 1. **Sentiment Distribution**
   - A pie chart illustrated the distribution of sentiments across all tweets. This showed the percentage of tweets categorized as positive, neutral, and negative.
   - The pie chart displays the distribution of sentiments. The largest portion is neutral at 50.6%, followed by positive sentiments at 35.3%, and negative sentiments are the smallest at 14.1%.
   - The bar plot provided a count-based comparison, making it clear which sentiment category was dominant in the data.
   - The bar chart displays the distribution of sentiments across three categories: Neutral, Positive, and Negative. The Neutral sentiment has the highest count, exceeding 40. Positive sentiment follows with a count slightly above 30, while Negative sentiment has the lowest count, around 10.

#### 2. **Sentiment Trend Over Time**
   - A line plot showed the sentiment trend over time, with an additional 3-month moving average line to smooth fluctuations. This allowed for a clearer view of changes in sentiment regarding Trump’s policies over the selected period.
   - It also displays the sentiment trend over time from April 2024 to November 2024. The sentiment score initially increases in May, peaks, and then drops sharply in June. It begins to recover in August and shows a positive trend by November.

#### 3. **Top Positive and Negative Tweets**
   - Based on sentiment scores, the top positive and negative tweets were identified:
     - **Top Positive Tweets**:
       - "What does Trump's win mean for International students?" (Sentiment: 0.2975)
       - "Trump implies that what's happening at college campuses is significant." (Sentiment: 0.2857)
     - **Top Negative Tweets**:
       - "The United States loses talent because of the policies." (Sentiment: -0.3000)
       - "According to USCIS, the average salary for an international student has dropped." (Sentiment: -0.1500).

#### 4. **Temporal Analysis: Heatmap**
   - A heatmap displayed the average sentiment scores by day of the week and month, allowing us to observe any day-specific patterns in sentiment expression.
   - The heatmap visualizes sentiment scores by the day of the week across different months from 2020 to 2024. Positive sentiment peaks at 0.29 on day 2 in May 2024. Notable negative sentiment is present at -0.14 on day 4 in June 2024. Overall, sentiment varies, with the highest positive and negative values occurring in 2024.

### Conclusion
The sentiment analysis on tweets concerning Trump’s policies suggests that there was a notable level of negative sentiment among users discussing the impact on international students, particularly Indian F1 students. The trend analysis indicated fluctuations in sentiment over time, with certain periods showing spikes in negative or positive sentiment, likely correlating with specific political events or policy announcements.

### Recommendations
- **Further Analysis**: This analysis could be expanded by including tweets from other relevant political figures or by performing a deeper topic modeling to understand specific concerns.
- **Comparison with Policy Changes**: Overlaying significant policy changes on the sentiment trend plot could provide insight into which events most impacted public sentiment.
- **Social Sentiment Insights**: Leveraging this data, universities and policymakers could gain insights into the public perception of immigration policies, helping guide communication strategies to international students.

### Visualizations
1. **Sentiment Distribution Pie Chart and Bar Plot**: Illustrated the overall sentiment breakdown.
2. **Sentiment Trend Line Plot**: Displayed changes over time, with a 3-month moving average for smoother trend visibility.
3. **Top Positive and Negative Tweets**: Highlighted specific tweets that were most positively or negatively perceived.
4. **Heatmap**: Showcased day-of-week and month patterns in sentiment, providing a temporal context for sentiment fluctuations. 

The analysis concludes that Trump’s policies had a noticeable impact on social sentiment among the international student community, particularly Indian F1 students in the U.S.
