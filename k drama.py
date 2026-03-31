import csv

def load_data():
    dramas = []
    try:
        with open("data.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                dramas.append(row)
    except FileNotFoundError:
        print("Dataset file not found!")
    return dramas


def recommend_by_genre(dramas, genre):
    results = [d for d in dramas if genre.lower() in d['Genre'].lower()]
    
    if not results:
        print("No dramas found for this genre.")
        return
    
    print("\nRecommended K-Dramas:\n")
    for i, drama in enumerate(results, start=1):
        print(f"{i}. {drama['Title']} (Rating: {drama['Rating']})")


def show_top_rated(dramas):
    sorted_dramas = sorted(dramas, key=lambda x: float(x['Rating']), reverse=True)
    
    print("\nTop Rated K-Dramas:\n")
    for i, drama in enumerate(sorted_dramas[:5], start=1):
        print(f"{i}. {drama['Title']} (Rating: {drama['Rating']})")


def main():
    dramas = load_data()
    
    while True:
        print("\n🎬 K-Drama Recommendation System")
        print("1. Recommend by Genre")
        print("2. Show Top Rated")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            genre = input("Enter genre (Romance, Action, Comedy, Thriller): ")
            recommend_by_genre(dramas, genre)
        
        elif choice == '2':
            show_top_rated(dramas)
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()