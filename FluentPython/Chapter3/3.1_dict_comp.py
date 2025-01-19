dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia')
]

contry_dial = {contry: code for code, contry in dial_codes }
print(contry_dial)

print(
    {
        code: contry.upper()
        for contry , code in sorted(contry_dial.items())
        if code < 70
    }
)
