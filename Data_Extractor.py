import re





class data_extractor():
    def __init__(self):
        self.collage_Pattern = self.get_pattern(r'\d+\S[a-zA-Z.,]+.+\s+(MBBS|BDS|B.Sc. Nursing)')
        self.re_initializer = self.get_pattern(r'^\d+')
        self.pattern_alloted_cat_ph_roundnum = self.get_pattern(r'(MBBS|BDS|B.Sc. Nursing)\s\w+\s\w+\s\d+')
        self.pattern_air_category = self.get_pattern(r'\d+\s\w+\s\d+\S')


    def get_collage_name(self,row_data):
        row_data = row_data.replace("\n"," ")


        match1 = self.collage_Pattern.finditer(row_data)
        for match in match1:
            start, end = match.span()
            coll_name = row_data[start:end]
            match = self.re_initializer.match(coll_name)
            re_initial = match.end()
            option_no = coll_name[0:re_initial]
            coll_name = coll_name[re_initial:].replace("MBBS", "")


        return coll_name,option_no

    def get_pattern(self, regex_pattern):
        pattern = re.compile(regex_pattern)
        return pattern

    def get_branch(self, row_info):
        try:
            if row_info.index("MBBS") >= 0:
                subject = "MBBS"
        except ValueError:
            pass
        try:
            if row_info.index("BDS") >= 0:
                subject ="BDS"
        except ValueError:
            pass
        return subject

    def get_alloted_cat_ph_roundnum(self, row_info):
        row_info = row_info.replace("\n"," ")
        matches = self.pattern_alloted_cat_ph_roundnum.finditer(row_info)
        for match in matches:
            start,end = match.span()
            data = row_info[start:end].split(" ")
            subject = data[0]
            alloted_category = data[1]
            alloted_ph = data[2]
            admitted_round = data[3]
        return subject,alloted_category,alloted_ph,admitted_round

    def get_air_category(self, row_info):
        row_info = row_info.replace("\n"," ")
        matches = self.pattern_air_category.finditer(row_info)
        for match in matches:
            start, end = match.span()
            data = row_info[start:end].split(" ")
            air = data[0]
            category = data[1]

        return air,category

    def get_quota_name(self, row_info):
        quota = ""
        row_info = row_info.replace("\n"," ")

        a = "Deemed/Paid Seats  Quota"
        b = "Non-Resident Indian"
        c = "Muslim Minority Quota"
        d = "All India"
        e = "Delhi University Quota"
        f = "IP University Quota"
        g = "Jain Minority Quota"
        h = "Open Seat Quota"
        i = "B.Sc Nursing All India"
        j = "Employees State Insurance Scheme(ESI)"
        try:
            if row_info.index(a) >= 0:
                    quota = a
            elif row_info.index(b) >= 0:
                    quota = b
            elif row_info.index(c) >= 0:
                    quota = c
            elif row_info.index(d) >= 0:
                    quota = d
            elif row_info.index(e) >= 0:
                    quota = e
            elif row_info.index(f) >= 0:
                    quota = f
            elif row_info.index(g) >= 0:
                    quota = g
            elif row_info.index(h) >= 0:
                    quota = h
            elif row_info.index(i) >= 0:
                    quota = i
                    print(quota)
            elif row_info.index(j)>=0:
                    quota = j
        except ValueError:
         pass

        return quota




