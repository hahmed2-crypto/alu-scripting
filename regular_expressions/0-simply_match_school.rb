#!/usr/bin/env ruby
# This script takes an argument and scans for the pattern "School"

puts ARGV[0].scan(/School/).join
