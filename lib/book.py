class Book:
    def __init__(this, title, page_count):
        this.title = title
        this._page_count = None  # Using a private attribute to enforce validation
        this.page_count = page_count  # This will call the setter method

    @property
    def page_count(this):
        return this._page_count

    @page_count.setter
    def page_count(this, value):
        if isinstance(value, int):
            this._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(this):
        print("Flipping the page...wow, you read fast!")
