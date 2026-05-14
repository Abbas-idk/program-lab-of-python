def add_numbers(*args):
    total = 0
    for num in args:
        if isinstance(num,(int,float)):
            total += num
        else:
            raise ValueError(f"Invalid type:{num} (must be int or float)")
    return total        
