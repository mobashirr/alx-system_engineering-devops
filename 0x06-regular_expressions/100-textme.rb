#!/usr/bin/env ruby
str =  ARGV[0].scan(/\[from:(?<sender>[^\]]+)\] \[to:(?<receiver>[^\]]+)\] \[flags:(?<flags>[^\]]+)\]/).join
puts str
