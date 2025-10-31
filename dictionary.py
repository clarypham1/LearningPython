def student_scores():
    scores = {"David" : 27,
          "Heidi" : 38,
          "Jim" : 79}
    scores ["Tom"] = 95

    scores["Jim"] = 75
    return scores
def top_student(scores):
    highest = max(scores, key=scores.get)
    return highest

final_scores = student_scores()
print(final_scores)

for name in final_scores:
    print(f"Student: {name}, scores {final_scores[name]}")

print(f"Top student is: {top_student(final_scores)}")