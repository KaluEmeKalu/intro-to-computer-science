class Student(object):
    def __init__(self, name="Kalu", age=28,
                 langs_known=["Python", "CSS", "HTML", "JAVASCRIPT", "JAVA"],
                 college_wish=["Harvard", "Stanford",
                               "MIT", "Yale", "Berkeley"],
                 years_studied=4,
                 embarrassing_story="I  peed my pants"
                 ):
        self.name = name
        self.age = age
        self.langs_known = langs_known
        self.years_studied = years_studied
        self.college_wish = college_wish
        self.embarrassing_story = embarrassing_story

    def make_list_string(self, a_list):
        s = ""
        for item in a_list[0:-1]:
            s += item + ", "
        s += 'and ' + a_list[-1]
        return s

    def make_intro(self):
        # add name
        text = "\n\nHello, my name is " + self.name + "."

        # add age
        text = text + " I am " + str(self.age) + " years old. "

        # add years_studed
        text += "I have studied programming for " + \
            str(self.years_studied) + " years. "

        # add langs known
        langs_str = self.make_list_string(self.langs_known)
        text += "In my years of studying, I have learned " + langs_str + ". "

        # add college_wish list
        college_str = self.make_list_string(self.college_wish)
        text += "For university, my dream schools are " + college_str + ". "

        # add embarrassing_story
        text += "I have an embarrassing story to share. One time " + \
            self.embarrassing_story + ". "

        # add conclusion
        text += "I hope you enjoyed getting to know me. Next time you can create your own student object."
        return text

s = Student(name="Kalu", age=28, langs_known=["Python", "CSS", "HTML", "JAVASCRIPT", "JAVA"],
            college_wish=["Harvard", "Stanford", "MIT", "Yale", "Berkeley"],
            years_studied=4, embarrassing_story="I  peed my pants")

s2 = Student(name="Ndukwe")
print(s2.make.intro(), s.make_intro())
