import time

print("=================================")
print("    Traffic Controller")
print("=================================")

while True:
    # RED LIGHT
    print("\nRED LIGHT")
    print("STOP -vehicles must wait")
    time.sleep(5)

    # GREEN LIGHT
    print("\nGREEN LIGHT")
    print("GO - vehicles can move")
    time.sleep(5)

    # YELLOW LIGHT
    print("\nYELLOW LIGHT")
    print("READY - Slow down")
    time.sleep(2)