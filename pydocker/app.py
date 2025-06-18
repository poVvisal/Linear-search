def linear_search(x, a):
    """Linear search algorithm implementation."""
    n = len(a)
    i = 1
    
    while i <= n and x != a[i-1]:
        i = i + 1
    
    if i <= n:
        location = i
    else:
        location = 0
    
    return location

def main():
    print("🔍 Interactive Linear Search Algorithm")
    print("=" * 50)
    
    # Sample data
    numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 492, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 2348, 100]
    
    print(f"📋 Available numbers: {numbers}")
    print("-" * 50)
    
    while True:
        try:
            # Get user input
            search_value = input("🎯 Enter a number to search for (or 'quit' to exit): ")
            
            # Check if user wants to quit
            if search_value.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            # Convert to integer
            search_value = int(search_value)
            
            print(f"\n🔍 Searching for: {search_value}")
            print("-" * 30)
            
            # Perform search
            result = linear_search(search_value, numbers)
            
            if result > 0:
                print(f"✅ SUCCESS: Value {search_value} found!")
                print(f"📍 Position: {result}")
                print(f"📍 Array index: {result-1} (0-based)")
                print(f"🔍 Steps taken: {result}")
            else:
                print(f"❌ NOT FOUND: Value {search_value} not in the list")
                print(f"🔍 Steps taken: {len(numbers)} (checked entire list)")
            
            print("-" * 50)
            
        except ValueError:
            print("❌ Please enter a valid number or 'quit' to exit")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except EOFError:
            print("\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()