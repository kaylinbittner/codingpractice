#Write a function to reverse a string (w/o using .reverse! method)

def reverse_string(string)
  string_split = string.split("")
  reordered = []
  string.size.times do
    reordered << string_split.pop
  end
  reordered.join
end
