from addition_file import Addition
import csv
import os
import sys

file_csv = os.getcwd() + '/films.csv'
file_obj = open(file_csv)
csv_reader = csv.reader(file_obj)
csv_data = list(csv_reader)


class SearchData:
    def __init__(self, count=0):
        self.count = count
        self.a = Addition('Class of 1999')

    def search_program(self):

        choice_main = input("Start the search(s), extend the csv-file(a) or exit(e)?: ")
        print()
        if choice_main == 's':
            choice_sub = input("Search by title(t), genre(g), sort by year(y) or return to main menu(r)?: ")
            print()
            if choice_sub == 't':
                title_input = input("Enter the movie title: ")
                print()

                tit_found = list(i[1] for i in csv_data[1:] if title_input.casefold() in i[1].casefold())

                if len(tit_found) > 1:
                    for self.count, s in enumerate(tit_found):
                        print(self.count + 1, s)

                    choice_tit_num = int(input("\nChoose the movie number: "))
                    print()
                    for k in csv_data[1:]:
                        if tit_found[choice_tit_num - 1] in k:
                            print(
                                f'imdb_id: {k[0]}\ntitle: {k[1]}\nyear: {k[2]}\npopularity: {k[3]}\ndescription: "{k[4]}"')
                            break

                elif len(tit_found) == 1:
                    print(tit_found[0])
                    print()
                    choice_mov = input("Receive the movie info(y) or return to main menu(n)?: ")
                    print()
                    if choice_mov == 'y':
                        for b in csv_data[1:]:
                            if tit_found[0] == b[1]:
                                print(
                                    f'imdb_id: {b[0]}\ntitle: {b[1]}\nyear: {b[2]}\npopularity: {b[3]}\ndescription: "{b[4]}"')
                                sys.exit()

                    elif choice_mov == 'n':
                        obj.search_program()

                    else:
                        print("Unknown command")
                        print()
                        obj.search_program()

                elif len(tit_found) == 0:
                    print("No such movie in the base")
                    print()
                    obj.search_program()

            elif choice_sub == 'g':
                genre_list = []
                for j in csv_data[1:]:
                    for dic in eval(j[16]):
                        genre_list.append(dic['genre'])

                new_genre_list = list(set(genre_list))
                new_genre_list.sort()

                genre_full = []
                for h in csv_data[1:]:
                    for gen_a in new_genre_list:
                        for gen_b in eval(h[16]):
                            if gen_a == gen_b['genre']:
                                genre_full.append(gen_a)

                genre_count = []
                print("Look what we have:")
                for elem in new_genre_list:
                    if elem in genre_full:
                        genre_count.append(genre_full.count(elem))
                        print(f'{self.count + 1}   {new_genre_list[self.count]}: ({genre_count[self.count]})')
                        self.count += 1
                print()

                self.count = 0
                choice_gen_num = int(input("Choose the number of movie genre: "))
                genre_titles = []
                for p in csv_data[1:]:
                    for dic in eval(p[16]):
                        if dic['genre'] == new_genre_list[choice_gen_num - 1]:
                            genre_titles.append(p[1])
                            print(f'{self.count + 1}   "{genre_titles[self.count]}"')
                            self.count += 1
                print()

                choice_mov_num = int(input("Choose the number of the movie: "))
                print()
                for f in csv_data[1:]:
                    if genre_titles[choice_mov_num - 1] in f:
                        print(
                            f'imdb_id: {f[0]}\ntitle: {f[1]}\nyear: {f[2]}\npopularity: {f[3]}\ndescription: "{f[4]}"')

            elif choice_sub == 'y':
                choice_tit_mov = int(input("Enter the Year: "))
                print()

                tit_found = list(i[1] for i in csv_data[1:] if choice_tit_mov == int(i[2]))

                if len(tit_found) > 1:
                    for v in csv_data[1:]:
                        for el in tit_found:
                            if el in v[1]:
                                print(self.count + 1, el, v[2])
                                self.count += 1

                    choice_tit_num = int(input("\nChoose the movie number: "))
                    print()
                    for k in csv_data[1:]:
                        if tit_found[choice_tit_num - 1] == k[1]:
                            print(
                                f'imdb_id: {k[0]}\ntitle: {k[1]}\nyear: {k[2]}\npopularity: {k[3]}\ndescription: "{k[4]}"')

                elif len(tit_found) == 1:
                    for h in csv_data[1:]:
                        if tit_found[0] == h[1]:
                            print(h[1], h[2])

                    film_data = input("\nChoose the current movie(m) or return to main menu(r)?: ")
                    print()
                    if film_data == 'm':
                        for b in csv_data[1:]:
                            if tit_found[0] == b[1]:
                                print(
                                    f'imdb_id: {b[0]}\ntitle: {b[1]}\nyear: {b[2]}\npopularity: {b[3]}\ndescription: "{b[4]}"')

                elif len(tit_found) == 0:
                    print("No movies with such year")
                    print()
                    obj.search_program()

            elif choice_sub == 'r':
                obj.search_program()

            else:
                print("Unknown command")
                print()
                obj.search_program()

        elif choice_main == 'a':
            question = input("Are you ready to extend csv-file? Otherwise return to main menu (y/n): ")
            print()
            if question == 'y':
                self.a.extend_csv_file()

            elif question == 'n':
                obj.search_program()

            else:
                print("Unknown command")

        elif choice_main == 'e':
            sys.exit()

        else:
            print("Unknown command")
            print()
            obj.search_program()


obj = SearchData()
obj.search_program()
