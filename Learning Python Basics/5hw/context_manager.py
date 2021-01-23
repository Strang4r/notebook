class Cntx_mngr:
    def __enter__(self):
        print("file opened")
        func.open()

    def __exit__(self, exc_type, exc_val, exc_tb):

        print("file closed...")
        func.close()