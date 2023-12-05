class TextFileRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def create(self, data):
        with open(self.file_path, "a") as file:
            file.write(data + "\n")

    def read_all(self):
        with open(self.file_path, "r") as file:
            return file.readlines()

    def find_by_id(self, target_id):
        try:
            lines = self.read_all()
            if 0 <= target_id < len(lines):
                return lines[target_id].strip()
        except Exception as e:
            raise ValueError(f"Failed to find data by ID: {e}")

    def update(self, index, new_data):
        lines = self.read_all()
        if 0 <= index < len(lines):
            lines[index] = new_data + "\n"
            with open(self.file_path, "w") as file:
                file.writelines(lines)

    def delete(self, index):
        lines = self.read_all()
        if 0 <= index < len(lines):
            del lines[index]
            with open(self.file_path, "w") as file:
                file.writelines(lines)
