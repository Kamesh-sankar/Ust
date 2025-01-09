def power(base,exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base,exponent-1)
  def tower_of_hanoi(n,source,destination,auxiliary):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    tower_of_hanoi(n-1,source,auxiliary,destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    tower_of_hanoi(n-1,auxiliary,destination,source)