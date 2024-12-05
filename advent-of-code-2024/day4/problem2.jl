1 + 1

data = readlines("input.in")

count = 0
valid = Set(["MS", "SM"])

for i in 2:(length(data)-1)
    for j in 2:(length(data[1])-1)
        if data[i][j] != 'A'
            continue
        end
        if ((data[i-1][j-1] * data[i+1][j+1]) in valid) && ((data[i-1][j+1] * data[i+1][j-1]) in valid)
            count += 1
        end
    end
end

count