

def read_instances():
    # Read the instance
    f = open("instance.txt", "r")
    instance_size = int(f.readline())
    instance = []
    for i in range(instance_size):
        row = f.readline().split(' ')

        for j in range(len(row)):
            if row[j].isdigit():
                instance.append(int(row[j]))
    f.close()

    return instance, instance_size

if __name__ == "__main__":
    instance, instance_size = read_instances()
    print(len(instance))
    print(instance_size)