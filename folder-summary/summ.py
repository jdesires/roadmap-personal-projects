import os
class Summarize:
    
    # Set the full path
    def full_path(self, file_name):
        # The folder this script is in
        script_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(script_dir, file_name)


    def directories(self, file_name):
        full_path = self.full_path(file_name)
        return os.listdir(full_path)
    
    def current(self, file_name):
            return os.getcwd()
    
    def size(self, full_path):
        pass
