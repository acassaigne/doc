
list_concat = fn (list_a, list_b) -> list_a ++ list_b end

res = list_concat.([1,2], [3,4])

#IO.puts res

sum = fn (a, b, c) -> a + b + c end

sum.(1, 2, 3)

pair_tuple_to_list = fn( a_tupple ) ->
  {a, b} = a_tupple
  [a,b]
end

print_len_list = fn
 ( [] ) -> IO.puts "It's an empty list !"
 ( [head | tail] ) ->
     len = 1 + length tail
     IO.puts "The lenght of list is #{len}"
end

