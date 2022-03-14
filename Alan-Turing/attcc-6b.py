letters = "pmniumbivekeshgwaxamrdteglachcollsdixaerxiwnqevlrhfmealflwptfkiwmwoftzztalasdjpbrratijgmdtulzeyualliwmheuwehxnvbzlfxayeglahgtdnnhlplouifnqmydpewqmnenafverhhthjsectndyisliwgmjrmhthrsaimhthanymhxljqdmjalyt"
numbers = "48456764437384546644438437736666483585767533486767883536344756588353685835657658347588583668877778544735734374776384763654365556874677845545543435686676667643533456738756487388773735383676855743434848668"
output = {3:"",4:"",5:"",6:"",7:"",8:""}
for i in range(len(letters)):
  output[int(numbers[i])]= output[int(numbers[i])] + letters[i]


print(output)
