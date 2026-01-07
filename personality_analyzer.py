from textblob import TextBlob

print("🧠 AI Personality Analyzer\n")

text = input("Enter any text: ")

blob = TextBlob(text)
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity

if polarity > 0.2:
    mood = "Positive 😊"
elif polarity < -0.2:
    mood = "Negative 😠"
else:
    mood = "Neutral 😐"

print("\n📊 Analysis Result")
print("Mood:", mood)
print("Emotion Strength:", round(abs(polarity) * 100, 2), "%")
print("Subjectivity:", round(subjectivity * 100, 2), "%")
