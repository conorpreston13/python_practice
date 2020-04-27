class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_bucket()

    def create_bucket(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    def get_val(self, key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No record found with this email address"

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = AlgoHashTable(256)
hash_table.set_val('conor@example.com', 'Conor Preston')
hash_table.set_val('melina@example.com', 'Melina Heredia')
hash_table.set_val('patrick@example.com', 'Patrick Preston')
hash_table.set_val('jill@example.com', 'Jill Preston')
hash_table.set_val('snickers@example.com', 'Snickers')
print(hash_table)
print(hash_table.get_val('conor@example.com'))
