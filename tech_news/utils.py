months = [
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]


def date_written_in_full(date):
    [year, month_el, day_el] = date.split("-")
    day = day_el if day_el[0] != "0" else day_el[1]
    month = months[int(month_el) - 1]
    return f"{day} de {month} de {year}"
