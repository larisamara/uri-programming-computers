note1, note2, note3, note4 = input().split()
average = ((float(note1) * 2) + (float(note2) * 3) + (float(note3) * 4) + (float(note4) * 1)) / 10
if (average >= 7.0):
    print("Media:", "%.1f" % average)
    print("Aluno aprovado.")
if (average < 5.0):
    print("Media:", "%.1f" % average)
    print("Aluno reprovado.")
if (average >= 5.0) and ( average <= 6.9):
    print("Media:", "%.1f" % average)
    print("Aluno em exame.")
    note_exame = float(input())
    print("Nota do exame:","%.1f" %  note_exame)
    average_end = (note_exame + average) / 2
    print("Aluno aprovado.")
    print("Media final:","%.1f" % average_end)