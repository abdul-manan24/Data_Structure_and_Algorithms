# Implementation of hash set in python.

class SimpleHashSet():
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, value):
        return sum(ord(char) for char in value) % self.size

    def add(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket

    def remove(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def print_set(self):
        print("Hash set contents:")

        for index, bucket in enumerate(self.buckets):
            print(f"Bucket: {index} : {bucket}")

my_hash_set = SimpleHashSet(10)

my_hash_set.add("Manan")
my_hash_set.add("Faraz")
my_hash_set.add("Khalique")
my_hash_set.add("Muttahar")
my_hash_set.add("Aneesa")
my_hash_set.add("Hanan")
my_hash_set.add("Inshrah")
my_hash_set.add("Fahad")
my_hash_set.add("Bob")
my_hash_set.add("Alison")

my_hash_set.print_set()

print(f"'Muttahar' in the set: {my_hash_set.contains("Muttahar")}")
print(f"Removing 'Muttahar'")
my_hash_set.remove("Muttahar")
print(f"'Muttahar' in the set: {my_hash_set.contains("Muttahar")}")

my_hash_set.print_set()