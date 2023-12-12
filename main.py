import dataprep
import scrapper


def main():
    main_list = dataprep.create_array()
    counter = 0

    for row in main_list:
        print(scrapper.get_data_web(
            row[0], row[0]+row[1], row[0]+row[1]+row[2]))
        counter += 1

    print("=================================")
    print(f"Cuenta: {counter}")
    print("=================================")
    print("Elementos en la lista: " + str(len(main_list)))


if __name__ == '__main__':
    main()
