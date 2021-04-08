import datetime

# Introducem doar numere intregi

def dayscount(month, year=None):
  if year==None:
    year = datetime.date.today().year
  if month <= 0 or year <= 0:
    return "Numerele introduse nu sant valide"
  if month > 12:
    if year <= 12:
      month, year = year, month
    else:
      return "Numerele introduse nu sant valide"
  leap = 0
  if year % 400 == 0:
    leap = 1
  elif year % 100 == 0:
    leap = 0
  elif year % 4 == 0:
    leap = 1
  if month==2:
    return 28 + leap
  list_odd_month = [1,3,5,7,8,10,12]
  if month in list_odd_month:
    return 31
  return 30

print(dayscount(2, 2000))
print(dayscount(2000, 2))