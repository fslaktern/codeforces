
from pwn import process

tests = len(range(2, 1001))
query_counts = {}
correct = wrong = 0
# context.log_level = "debug"
# r = process("./main.py")
r = process("./target/release/ruler-easy")
r.sendline(str(tests).encode("utf-8"))

for answer in range(2, 1000):
    found = False
    ruler = list(range(1000))
    del ruler[answer]
    query_count = 0
    data = f"Answer should be {answer}"
    
    while not found:
        query = r.recvline()
        query = query[:-1].decode("utf-8").split()
        while query[0] == "#":
            data += "\n" + " ".join(query)
            query = r.recvline()
            query = query[:-1].decode("utf-8").split()
        assert 1 < len(query) < 4

        if query[0] == "?":
            query_count += 1
            a, b = int(query[1]), int(query[2])
            response = ruler[a] * ruler[b]
            r.sendline(str(response).encode("utf-8"))
        elif query[0] == "!":
            found = True
            if str(query_count) in query_counts:
                query_counts[str(query_count)] += 1
            else:
                query_counts[str(query_count)] = 1
            if int(query[1]) == answer:
                data += f"\nCorrect answer: {query[1]} - {query_count} queries\n"
                correct += 1
                print(data)
                # if query_count == 8:
            else:
                data += f"\nWrong answer: {query[1]} - {query_count} queries\n"
                wrong += 1
                print(data)
                exit(1)
        else:
            data += "\n" + f"Got invalid symbol {query[0]}"

print(f"{correct=}\n{wrong=}")
[print(f"{k}: {v}") for k, v in sorted(query_counts.items())]
