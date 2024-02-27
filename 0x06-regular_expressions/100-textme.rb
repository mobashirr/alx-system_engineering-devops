#!/usr/bin/env ruby

# Use scan to find all matches of the regex pattern in the input string
matches = ARGV[0].scan(/\[from:(?<sender>[^\]]+)\] \[to:(?<receiver>[^\]]+)\] \[flags:(?<flags>[^\]]+)\]/)

# Iterate over each match
matches.each do |match|
  # Extract sender, receiver, and flags from the current match
  sender = match[0]
  receiver = match[1]
  flags = match[2]

  # Output the extracted information
  puts "#{sender},#{receiver},#{flags}"
end
