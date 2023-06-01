# Example : Repeated Code Blocks
# DRY

def greet(name):
    print(f'Hello, {name}!')


greet('Snape')
greet('Malfoy')
greet('Bellatrix')

# WET

print('Hello,Snape!')
print('Hello, Malfoy!')
print('Hello, Bellatrix!')
