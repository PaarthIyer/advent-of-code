function main()
    input_file = "./input.in"

    data = readlines(input_file)

    split_at = findfirst(isequal(""), data)

    rules_raw = data[1:split_at-1]
    rules = Set(parse.(Int, split(x, "|")) for x in rules_raw)

    print_list = data[split_at+1:end]
    print_list = [parse.(Int, split(x, ",")) for x in print_list]

    function comp(a, b)
        [a, b] in rules && return 1
        [b, a] in rules && return -1
        return 0
    end

    function valid_order(ls)
        for i in eachindex(ls), j in ls[1:i-1]
            if comp(ls[i], j) < 0
                return true
            end
        end
    end

    println(valid_order(print_list[2]))
    println(valid_order(print_list[3]))
    println(valid_order(print_list[4]))
    println(valid_order(print_list[5]))
end

main()