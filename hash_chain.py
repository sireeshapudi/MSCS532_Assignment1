class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # update existing key
                return
        
        bucket.append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# -------------------------------
# Testing Hash Table
# -------------------------------
ht = HashTableChaining()

ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("orange", 30)
ht.insert("grapes", 40)

print("Hash Table after insertion:")
ht.display()

print("\nSearch for 'banana':", ht.search("banana"))

print("\nDelete 'banana':", ht.delete("banana"))

print("\nHash Table after deletion:")
ht.display()
