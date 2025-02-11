
from datetime import datetime
clock = datetime.now()
ans = 24*2
ans += 24 - clock.hour 
ans -= 1 #Check's back agaisn the fact we're continuing this hour 
print(ans)