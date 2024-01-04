from pprint import pprint
import csv
import os
import sys

file_csv = os.getcwd() + '/films.csv'
file_obj = open(file_csv)
csv_reader = csv.reader(file_obj)
csv_data = list(csv_reader)


# pprint(csv_data)


class SearchData:
    def __init__(self, count=0):
        self.count = count

    def count_func(self):

        count_list = [el for el in range(1, self.count + 1)]
        return count_list

    def search_program(self):

        choice_main = input("Start the search(s) or exit(e)?: ")
        print()
        if choice_main == 's':
            choice_sub = input("Search by title(t) or genre(g), or return to main menu(r)?: ")
            print()
            if choice_sub == 't':
                title_input = input("Enter the movie title (перше слово має бути з великої лiтари, наступнi, крiм 'of', 'the', 'to', тощо, теж з великої): ")
                print()

                tit_found = []
                for i in csv_data[1:]:
                    if title_input in i[1]:
                        print(self.count + 1, i[1])
                        self.count += 1

                        tit_found.append(i[1])

                choice_tit_num = int(input("\nChoose the movie number: "))
                print()
                for k in csv_data[1:]:
                    for num in obj.count_func():
                        if num == choice_tit_num:
                            if tit_found[num - 1] in k:
                                print(f'imdb_id: {k[0]}\ntitle: {k[1]}\nyear: {k[2]}\npopularity: {k[3]}\ndescription: "{k[4]}"')

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
                    for num in obj.count_func():
                        if num == choice_mov_num:
                            if genre_titles[num - 1] in f:
                                print(f'imdb_id: {f[0]}\ntitle: {f[1]}\nyear: {f[2]}\npopularity: {f[3]}\ndescription: "{f[4]}"')

            elif choice_sub == 'r':
                obj.search_program()

            else:
                print("Unknown command")

        elif choice_main == 'e':
            sys.exit()

        else:
            print("Unknown command")
            obj.search_program()


obj = SearchData()
obj.search_program()