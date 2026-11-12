from datetime import date

event_date = date(2026, 12, 31)
today = date.today()

if event_date > today:
    difference = event_date - today
    print("До події залишилося днів:", difference.days)
elif event_date < today:
    difference = today - event_date
    print("Після події минуло днів:", difference.days)
else:
    print("Подія відбувається сьогодні!")
