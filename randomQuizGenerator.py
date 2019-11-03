#! python3
# randomQuizGenerator.py - Create quizzer with questions and answers in
# random order, along with the answer key.

import random
import usCapitals

capitals = usCapitals.capitals

# Generate 35 quiz files.

for quizNum in range(35):
  # Create the quiz and answer key files.
  quizFile = open('capitalsquiz%s.txt' % (quizNum+1), 'w')
  answerKeyFile = open('capitalquiz_answers%s' % (quizNum+1), 'w')

  # Write out the header for the quiz.
  quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
  quizFile.write((' ' * 20)) + 'State Capitals Quiz (form %s)' % (quizNum + 1)
  quizFile.write('\n\n')

  quizFile.close()
  answerKeyFile.close()

