def getHashTagsFromFile(self):
    with open(self.hash_dir, "r") as f:
        lines = f.readlines()
        temp =[]
        for line in lines:
            line = line.replace("\n", "")
            temp.append(line)
            temp.append(" ")
        lines = temp
    return lines