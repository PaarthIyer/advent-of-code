function func()# Input file
    input_file = "./input.in"

    # Read file content
    data = read(input_file, String)

    # Define the regex pattern
    valid_re = r"mul\((\d+),(\d+)\)"

    # Extract numbers using regex and calculate summation

    @time begin
        summ = sum(
            parse(Int, m.captures[1]) * parse(Int, m.captures[2]) for m in eachmatch(valid_re, data)
        )
    end
    print(summ)
end

func()