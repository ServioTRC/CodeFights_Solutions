def lateRide(n):
    hours = n // 60
    minutes = n - hours*60
    return(hours//10 + hours%10 + minutes//10 + minutes%10)