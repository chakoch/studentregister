def print_menu(choice, message):
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Ogiltigt val, försök igen.")
        return False
    print(f"Du valde alternativ nummer {choice}. {message}")
    return True

def add_student(students):
    print_menu("1", "Lägger till en ny student.\n")
    student_name = input("Ange studentens namn: ").strip()

    while True:
        new_age = input("Ange ålder (1 - 99): ").strip()
        if new_age.isnumeric() and 1 <= int(new_age) <= 99:
            age = int(new_age)
            print(f"✅ Ålder satt till {age}.")
            break
        print("❌ Ogiltig ålder. Försök igen.")


    raw = input("Ange favoritämnen: ").split(",")
    favoritämnen = [s.strip() for s in raw if s.strip()]
    students.append({"namn": student_name, "ålder": age, "favoritämnen": favoritämnen})
    print(f"✅ {student_name} tillagd.")

def list_students(students):
    print_menu("2", "Visar alla registrerade studenter.\n")
    if not students:
        print("Inga studenter registrerade.")
        return
    for i, s in enumerate(students, start=1):
        favo = ", ".join(s["favoritämnen"]) if s["favoritämnen"] else "—"
        print(f"{i}. {s['namn']} – {s['ålder']} år – Favoritämnen: {favo}")

def search_student(students):
    print_menu("3", "Sök student.\n")
    name = input("Ange namn för att söka: ").strip()
    for s in students:
        if s["namn"].lower() == name.lower():
            favo = ", ".join(s["favoritämnen"]) if s["favoritämnen"] else "—"
            print(f"✅ Hittade: {s['namn']} – {s['ålder']} år – Favoritämnen: {favo}")
            return
    print("\n❌ Ingen student med det namnet hittades.")

def average_age(students):
    print_menu("4", "Beräkna genomsnittsålder.\n")
    if not students:
        print("----- INGA REGISTRERADE STUDENTER -----")
        return
    ages = []
    for s in students:
        try:
            ages.append(int(s["ålder"]))
        except (KeyError, ValueError):
            pass
    if ages:
        avg_age = sum(ages) / len(ages)
        print(f"ℹ️ Genomsnittsålder: {avg_age:.1f} år ({len(ages)})\n")
    else:
        print("Inga giltiga åldrar registrerade.")

def remove_student(students):
    print_menu("5", "Ta bort student.\n")
    name = input("Ange namn på studenten som ska tas bort: ").strip()
    for i, s in enumerate(students):
        if s["namn"].lower() == name.lower():
            del students[i]
            print(f"✅ {name} har tagits bort.")
            return
    print(f"\n❌ Ingen student med det namnet {name} hittades.")

def main():
    students = []
    print("🎓 Välkommen till Studentregistret!")
    while True:
        print("\n======= Meny =======")
        print("1) Lägg till student")
        print("2) Lista alla studenter")
        print("3) Sök student")
        print("4) Genomsnittsålder")
        print("5) Ta bort student")
        print("6) Avsluta")
        choice = input("Välj [1-6]: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            average_age(students)
        elif choice == "5":
            remove_student(students)
        elif choice == "6":
            print("👋 Hejdå!")
            break
        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    main()