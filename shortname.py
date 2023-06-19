import re


# Converted from https://github.com/speechanddebate/tabroom/blob/ff241f2f760257d7964750d0e30ffa2f3034c931/web/funclib/short_name.mas
def short_school_name(name):
    if name is None: return None

    name = name.rstrip('\n')
    name = name.replace('.', '')
    name = name.rstrip()  # trailing spaces

    if name.lower() == "thomas jefferson high school of science and technology":
        name = "Thomas Jefferson"
    elif name.lower() == "thomas jefferson high school of science & technology":
        name = "Thomas Jefferson"
    elif name.lower() == "the bronx high school of science":
        name = "Bronx Science"
    elif name.lower() == "whitney m. young magnet high school":
        name = "Whitney Young"
    elif name.lower() == "lane tech college prep h.s.":
        name = "Lane Tech"
    elif name == "New School":
        name = "NewSkool"
    elif name == "The New School":
        name = "NewSkool"
    elif name == "BC Academy":
        name = "BCAC"

    if name == "Air Academy High School" or name == "Air Academy HS":
        name = "AirAcademy"

    if name == "Milton Academy" or name == "MiltonAcademy":
        name = "Milton Acad"

    if name == "Milton High School" or name == "MiltonHigh" or name == "Milton HS":
        name = "Milton High"

    if name == "Cary Academy":
        name = "Cary Acad"
    elif name == "Cary High School":
        name = "Cary High"
    elif name == "Cary HS":
        name = "Cary High"

    name = name.replace("College Prep H.S.", "")
    name = name.replace("College Prep HS", "")
    name = name.replace("College Prep High School", "")
    name = name.replace("College Prep", "CP")

    if name == "Boston College":
        name = "BC"
    elif name == "Boston University":
        name = "BU"

    name = name.replace("/", " ")

    name = name.replace(" Mock Trial", "")
    name = name.replace(" Debate Association", "")
    name = name.replace(" Debate Panel", "")
    name = name.replace(" Debate Society", "")
    name = name.replace(" Debating Society", "")
    name = name.replace(" Forensics/Debate", "")
    if name == "New York University": name = "NYU"
    name = name.replace(" of Math and Science", "")
    name = name.replace(" Academy", "")
    name = name.replace(" Regional High School", "")
    name = name.replace(" High School", "")
    name = name.replace(" Colleges", "")
    name = name.replace(" School", "")
    name = name.replace(" school", "")
    name = name.replace(" Schools", "")
    name = name.replace(" schools", "")
    name = name.replace(" High", "")
    name = name.replace(" Junior-Senior", "")

    name = name.rstrip()  # trailing spaces
    name = name.rstrip('.')

    name = name.replace(" H.S", "")
    name = name.replace(" HS", "")
    name = name.replace(" M.S", "")
    name = name.replace(" MS", "")
    name = name.replace(" (MS)", "")
    name = name.replace(" JH", "")
    name = name.replace(" Jr", "")
    name = name.replace(" JR", "")
    name = name.replace(" Middle", "")
    name = name.replace(" (Middle)", "")
    name = name.replace(" Elementary", "")
    name = name.replace(" (Elementary)", "")
    name = name.replace(" Intermediate", "")
    name = name.replace(" Community", "")
    name = name.replace(" (Intermediate)", "")
    name = name.replace(" Junior", "")
    name = name.replace(" Middle School of the Arts", " Arts")
    name = name.replace(" School of the Arts", " Arts")
    name = name.replace(" (Middle)", "")
    name = name.replace("Regional", "")
    name = name.replace(" Academy", "")
    name = name.replace(" School", "")
    name = name.replace(" school", "")
    name = name.replace(" Schools", "")
    name = name.replace(" schools", "")
    name = name.replace(" Sr", "")
    name = name.replace(" sr", "")

    name = name.replace(" Preparatory", " Prep")

    name = name.replace(" Club", "")
    name = name.replace(" Team", "")
    name = name.replace(" Society", "")
    name = name.replace(" Speech and Debate", "")
    name = name.replace(" Forensics", "")
    name = name.replace(" Forensic", "")
    name = name.replace(" Speech", "")
    name = name.replace(" Debate", "")
    name = name.replace(" &", "")
    name = name.replace(" and", "")
    name = name.replace(" +", "")
    name = name.replace(" Parliamentary", "")

    name = name.replace("Public Charter", "")
    name = name.replace(" Charter Public", "")
    name = name.replace("The University of", "")
    name = name.replace("The University Of", "")
    name = name.replace("University of", "")
    name = name.replace("University Of", "")
    name = name.replace("The College of", "")
    name = name.replace("The College Of", "")
    name = name.replace("College of", "")
    name = name.replace("College Of", "")
    name = name.replace("Technological", "Tech")
    name = name.replace("Technology", "Tech")
    name = name.replace("Community College", "Community")
    name = name.replace("California State University,", "CSU")
    name = name.replace("California State University", "CSU")
    name = name.replace("State University", "State")
    name = name.replace("California,", "UC")
    name = name.replace(" University", "")
    name = name.replace(" College", "")
    name = name.replace(" CC", "")
    name = name.replace("State University,", "State ")

    name = name.strip()

    return name


def substr(s: str, n: int):
    return s[:min(len(s), n)]


# Converted from https://github.com/speechanddebate/tabroom/blob/ff241f2f760257d7964750d0e30ffa2f3034c931/web/funclib/chapter_code.mas
def chapter_code(school_code):
    if school_code is None: return None

    school_code = school_code.replace('-', ' ')
    school_code = school_code.replace(',', ' ')
    school_code = school_code.replace('.', '')
    school_code = school_code.replace('  ', ' ')
    school_code = school_code.replace('  ', ' ')
    school_code = re.sub(r'[^\w\s]', '', school_code)

    if school_code == "Hendrick Hudson":
        school_code = "HenHud"
    elif school_code == "Newton South":
        school_code = "NewtnS"
    elif school_code == "Newton North":
        school_code = "NewtnN"
    elif school_code == "Newtown":
        school_code = "Newtwn"
    elif school_code == "Lexington":
        school_code = "Lexton"
    elif school_code == "Bronx Science" or school_code == "Bronx HS of Science":
        school_code = "BrxSci"
    elif school_code == "Newburgh Free Academy":
        school_code = "NFA"
    elif school_code == "Walt Whitman":
        school_code = "Whitmn"
    elif school_code == "Byram Hills":
        school_code = "Byram"
    elif school_code == "Scarsdale":
        school_code = "ScsDle"
    elif school_code == "University":
        school_code = "USchool"
    elif school_code == "Strake Jesuit College Prep":
        school_code = "Strake"

    school_code = re.sub(r'ington$', 'ton', school_code)
    school_code = re.sub(r'University Of |University of ', 'U', school_code)
    school_code = re.sub(r'University$', 'U', school_code)

    spaceless = re.sub(r'[\W_]', '', school_code)

    if len(spaceless) < 7:
        school_code = spaceless
    elif ' ' in school_code:
        bits = school_code.split(' ')
        if len(bits) > 3:
            school_code = ''
            for bit in bits:
                if bit:
                    letter = bit[0]
                    school_code += letter.upper()
            school_code = substr(school_code, 6)
        else:
            school_code = substr(bits[0], 3) + substr(bits[1], 3)
    else:
        school_code = substr(school_code, 6)

    school_code = re.sub(r'\s', '', school_code)

    return school_code
