require 'date'
require 'yaml'

SSN_PATTERN = /^(?<gender>[12])\s?(?<birthyear>\d{2})\s?(?<birthmonth>0[1-9]|1[0-2])\s?(?<department>\d{2})\s?\d{3}\s?\d{3}\s?(?<key>\d{2})$/


def french_ssn_info(ssn)
  match_data = ssn.match(SSN_PATTERN) #Comparing a string to a regular expression
  if match_data #Should read this line as, "If match_data exists..." (NOT NIL || FALSE)
    gender = detect_gender(match_data[:gender].to_i)
    month = Date::MONTHNAMES[match_data[:birthmonth].to_i]
    year = "19" + match_data[:birthyear]
    department = YAML.load_file('./data/french_departments.yml')[match_data[:department]] #I dont have this file, but this is how you would link it if I did - INFO stored as hash
    return "A #{gender}, born in #{month}, #{year} in #{department}."
  else
    return "The number is invalid"
end

def detect_gender(number)
  if number == 1
    return 'man'
  else
    return 'woman'
  end
