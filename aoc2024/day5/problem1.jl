function main()
    input_file = "./input.in"

    data = readlines(input_file)

    split_at = findfirst(isequal(""), data)

    rules_raw = data[1:split_at-1]
    rules = Set(parse.(Int, split(x, "|")) for x in rules_raw)

    print_list = data[split_at+1:end]
    print_list = [parse.(Int, split(x, ",")) for x in print_list]

    function comp(a, b)
        if [a, b] in rules
            return 1
        end
        if [b, a] in rules
            return -1
        end
        return 0
    end

    function valid_order(ls)
        for i in eachindex(ls), j in ls[i+1:end]
            if comp(ls[i], j) < 0
                return false
            end
        end
        return true
    end

    total_sum = 0

    for pl in print_list
        if valid_order(pl)
            total_sum += pl[(length(pl)+1)÷2]
        end
    end

    return total_sum
end

@time answer = main()

print(answer)