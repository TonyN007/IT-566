from person import Person
from student import Student

def main():
    # Create instance of Person
    p1 = Person('Tony', 'J','Nguyen')
    print(f'p1 = {p1.first_name}')


    s1 = Student('Tony', 'J', 'Nguyen', '0194826', 'Cybersecurity')
    print(f's1.first_name: {s1.first_name} Major: {s1.major}')
    print(f'{s1}')


if __name__ == '__main__':
    main()