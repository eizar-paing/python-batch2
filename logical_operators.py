# 0 0 => 0
# 0 1 => 2**0 = 1
# 1 0 => 2**1 = 2
# 1 1 => 2**1 + 2**0 = 3

# AND (&&)
# 0 0 => false && false = false => 0
# 0 1 => false && true = false => 0
# 1 0 => true && false = false => 0
# 1 1 => true && true = true => 1

# OR (||)
# 0 0 => false || false => false => 0
# 0 1 => false || true => true => 1
# 1 0 => true || false => true => 1
# 1 1 => true || true => true => 1

a = 101
if(a > 1 and a <100) => 
if (True and False) => False

b = 20
if((b%2) == 0 or b < 100) => True