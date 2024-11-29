class Shoe:
    def __init__(this, brand, size):
        this.brand = brand
        this._size = None  # Private attribute for size validation
        this.size = size   # This will call the setter method
        this.condition = None  # Initially unset

    @property
    def size(this):
        return this._size

    @size.setter
    def size(this, value):
        if isinstance(value, int):
            this._size = value
        else:
            print("size must be an integer")

    def cobble(this):
        this.condition = "New"  
        print("Your shoe is as good as new!")
