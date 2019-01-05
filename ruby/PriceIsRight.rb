price = (rand(100))

puts 'What do you think the price of this item is?'
user_guess = gets.chomp.to_i

while guess != price
  if guess > price
    puts "Your guess is higher than the price!"
  else
    puts "Your guess is too low!"
  end
  puts 'What do you think the price of this item is?'
  user_guess = gets.chomp.to_i
end

puts "You won, the price was #{{price}}"
