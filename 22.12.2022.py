

print(chislo(7))
# З Здадача



class Themes:
    def __init__(self, themelst):
        self.themelst = themelst

    def add_theme(self, addtheme):
        self.addtheme = addtheme
        self.themelst.append(addtheme)
        return self.themelst

    def shift_one(self, addtheme1):
        self.addtheme1 = addtheme1
        self.themelst = self.themelst[::-1]
        self.themelst.append(addtheme1)
        self.themelst = self.themelst[::-1]
        return self.themelst

    def reversed_order(self):
        self.themelst = self.themelst[::-1]
        return self.themelst

    def get_items(self):
        return self.themelst

    def get_first(self):
        return self.themelst[0]

themes = Themes(['Standoff', 'sport', 'health'])

print(themes.get_items())

print(themes.get_first())

print(themes.reversed_order())

print(themes.add_theme('Thene'))

print(themes.shift_one('draw'))
