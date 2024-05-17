arr = []

with open("nyc_weather.csv", "r") as f:
    for line in f:
        try:
            temperature = line.split(",")[1]
            arr.append(int(temperature))
        except:
            pass

print(arr)
print(f"Average temperature of first week of Jan {sum(arr[:7])/len(arr[:7])}")

print(f"Maximum temperature in first 10 days {max(arr[:11])}")

weather_dict = {}
with open("nyc_weather.csv", "r") as f:
    for line in f:
        try:
            tokens = line.split(",")
            key = tokens[0]
            value = int(tokens[1])
            weather_dict[key] = value
        except:
            pass

print(f"Weather Dictionary {weather_dict}")
print(f"Temperature on Jan 9 {weather_dict['Jan 9']}")
print(f"Temperature on Jan 4 {weather_dict['Jan 4']}")


# Problem 3
word_count = {}

with open("poem.txt", "r") as f:
    for line in f:
        for token in line.split(" "):
            token = token.strip()
            if token.endswith("."):
                token = token[:-1]
            if token in word_count:
                word_count[token] = word_count[token] + 1
            elif token:
                word_count[token] = 1

print(word_count)
