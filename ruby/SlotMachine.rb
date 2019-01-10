class SlotMachine

ITEMS = {"joker" => [50, 25],
        "star" => [40, 20],
        "bell" => [30, 15],
        "seven" => [20, 10],
        "cherry" =>[10, 5] }.freeze

  def score(reels)
    if reels.uniq.length == 1
      items[reels.first].first
    elsif reels.uniq.length == 2 && reels.count("joker") == 1
      reels = reels.delete("joker")
      items[reels.first].last
    elsif reels.uniq.length == 2 && reels.count("joker") == 2
      return 25
    elsif reels.uniq.length == 3
      return 0
    end
  end
end
