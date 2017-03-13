import csv
import random
import nltk


class GenderPredictor:

    def get_features(self):
        names = self._load_names()
        male_names = names['male']
        female_names = names['female']
        featureset = list()

        for male_name in male_names:
            features = self._name_features(male_name)
            featureset.append((features, 'M'))

        for female_name in female_names:
            features = self._name_features(female_name)
            featureset.append((features, 'F'))

        return featureset

    def train_and_test(self, training_percent=0.90):
        featureset = self.get_features()
        random.shuffle(featureset)

        name_count = len(featureset)
        cut_point = int(name_count * training_percent)

        train_set = featureset[:cut_point]
        test_set = featureset[cut_point:]

        self.train(train_set)

        return self.test(test_set)

    def classify(self, name):
        feats = self._name_features(name)
        return self.classifier.classify(feats)

    def train(self, train_set):
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)
        return self.classifier

    def test(self, test_set):
        return nltk.classify.accuracy(self.classifier, test_set)

    def _load_names(self):
        names = dict()
        names['male'] = list()
        names['female'] = list()
        with open('ismlar.csv') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                names[row[0]].append(row[1])

        return names

    def _get_prob_distr(self, name_tuple):
        male_prob = (name_tuple[1] * 1.0) / (name_tuple[1] + name_tuple[2])

        if male_prob == 1.0:
            male_prob = 0.99
        elif male_prob == 0.0:
            male_prob = 0.01
        else:
            pass

        female_prob = 1.0 - male_prob
        return (male_prob, female_prob)

    def get_most_informative_features(self, n=5):
        return self.classifier.most_informative_features(n)

    def _name_features(self, name):
        name = name.upper()
        return {
            'last_letter': name[-1],
            'last_two': name[-2:],
            'last_three': name[-3:],
            'last_four': (lambda: name[-4:] if len(name) >= 4 else name)(),
            'first_three': name[:3],
            'first_four': (lambda: name[:-4] if len(name) >= 4 else name)(),
            'last_is_vowel': (name[-1] in 'AEIOU')
        }


if __name__ == '__main__':
    gp = GenderPredictor()
    accuracy = gp.train_and_test()
    print('Аниқлик даражаси: ', round(accuracy, 2))

    while True:
        name = input('Текшириш учун исм киритинг: ')
        
        if name in 'qQ' or name == 'exit':
            break

        _ = {
            'M': 'эркаклар',
            'F': 'аёллар'
        }
        predicted_gender = _[gp.classify(name)]
        print(
            '{name} исми тахмин бўйича {gender} исми.'.format(
                name=name,
                gender=predicted_gender))
