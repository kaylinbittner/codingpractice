# Days til Christmas, from any date, until the next Christmas (not date specific)

require 'date'

def days_until_christmas(date)
  xmas_day = Date.new(date.year, 12, 25)
  
  if date > xmas_day
     xmas_day = Date.new(year + 1, 12, 25)
  end
  
  difference = xmas_day - date
  return difference.to_i
end
