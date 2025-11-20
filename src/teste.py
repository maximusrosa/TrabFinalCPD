import cProfile
import pstats
from fifa_database import FIFA_Database

def main():
    fifa_db = FIFA_Database()
    fifa_db.get_players_info()

    with cProfile.Profile() as pr:
        fifa_db.get_rating_info('../data/rating.csv')


    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    #stats.print_stats()

    stats.dump_stats(filename='../output/rating_stats.prof')


if __name__ == '__main__':
    main()
