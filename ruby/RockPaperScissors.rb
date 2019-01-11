options = ["Rock", "Paper", "Scissors"]
computer_hand = options.sample


#LONG HAND
if computer_hand == user_input
  puts "That's a Draw Partner"
elsif computer_hand == "Rock"
   if user_input == "Paper"
     puts "That's a Win Partner"
   else
    puts "Aw Shucks, You Lost!"
  end
end

#SHORT HAND

if computer_hand == "Rock"
  user_input == "Paper" ? "You Win Partner" : "Aw Shucks, You Lost!"
end

# Loop to Check User Input is Valid

user_input = ''
until options.include?(user_input)
  puts "Rock, Paper, Scissors?"
  user_input = gets.chomp
end
