import os

import profilescraper
import profilepersistence


class ProfileConstructor:

    def _in_database(self, id):
        return os.path.exists(os.getcwd() + '/database/%s.csv' % id)

    def construct(self, id):
        if self._in_database(id):
            return profilepersistence.ProfilePersistence.load(id)
        else:
            scraper = profilescraper.ProfileScraper(id)
            data = scraper.scrap()
            profilepersistence.ProfilePersistence.save(id, data)
            return data


def main():
    constructor = ProfileConstructor()
    print(constructor.construct('36720'))


if __name__ == '__main__':
    main()