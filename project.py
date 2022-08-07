import random
import pandas as pd

import sys


def entry_data():
    df1 = pd.read_csv("medical_report.csv")

    # ads a value of predicted disease to a mediacl report template,
    # filtered for a more serious probability of disease over 55 %

    inside2 = {
        'Diabetes': round(random.uniform(0.33, 99.66), 2),
        'Depression ': round(random.uniform(0.33, 99.66), 2),
        'Anxiety ': round(random.uniform(0.33, 99.66), 2),
        'Yeast infection ': round(random.uniform(0.33, 99.66), 2),
        'Lupus ': round(random.uniform(0.33, 99.66), 2),
        'Shingles ': round(random.uniform(0.33, 99.66), 2),
        'Psoriasis ': round(random.uniform(0.33, 99.66), 2),
        'Heart disease ': round(random.uniform(0.33, 99.66), 2),
        'Alzheimer': round(random.uniform(0.33, 99.66), 2),
        'Haemophilia ': round(random.uniform(0.33, 99.66), 2),
        'Pneumonia': round(random.uniform(0.33, 99.66), 2),
        'HPV ': round(random.uniform(0.33, 99.66), 2),
        'Strep throat ': round(random.uniform(0.33, 99.66), 2),
        'Bronchitis': round(random.uniform(0.33, 99.66), 2),
        'Lyme ': round(random.uniform(0.33, 99.66), 2),
        'Liver poison ': round(random.uniform(0.33, 99.66), 2),
        'ADHD ': round(random.uniform(0.33, 99.66), 2),
        'Dementia ': round(random.uniform(0.33, 99.66), 2),
        'Autism ': round(random.uniform(0.33, 99.66), 2),
    }
    newDict = {key: value for (key, value) in inside2.items() if value > 50}
    df1['dis'] = pd.NaT
    df1['dis'] = df1['dis'].apply(lambda x: newDict)
    return df1


def entry_data2(df1):
    df2 = pd.read_csv("meds_list.csv")

    C = df2['rating'].mean()

    m = df2['bought'].quantile(0)

    q_product = df2.copy().loc[df2['bought'] >= m]

    # adding waithed rating
    q_product['score'] = q_product.apply(weighted_rating, axis=1, args=(m, C))

    # transforming product list sorted by score with ordered columns
    q_product = q_product.sort_values('score', ascending=False)
    df2 = q_product[['pro_name', 'type', 'desc', 'rating', 'bought', 'dis', 'score']]

    diagnosis = df1.values.tolist()
    meds = df2.values.tolist()

    for diag in diagnosis:
        """
        Showning result of patient disorders report match with recomended products.
        Args:
            patient disorders
            matched best products
        Print:
            Result of match as a medical report
        """
        disorders = diag[6]
        print("Name: " + str(diag[2]) + " " + str(diag[3]))
        print('Date: ' + str(diag[1]))
        print('Age: ' + str(diag[4]))
        print('Gender: ' + str(diag[5]))

        print("Disorders: " + str(disorders))
        best_meds = run_search(disorders, meds, 4)
        print("")
        print("Recomended meds products for disorders:")
        for med in best_meds['meds']:
            print(med)
        return 0


def weighted_rating(x, m, C):
    """
    Calculates weighted score of a product
    Args:
        number of product purchases - mocked data
        product review - mocked data
    Return:
        weighted score
    """
    v = x['bought']
    R = x['rating']
    res = (v / (v + m) * R) + (m / (m + v) * C)
    return res


def compare_scores(ncures, disorders):
    # print("1: " + str(ncures))
    # print("1: " + str(disorders))
    """
    Calculates the final result as the sum of multiplied arguments
    Args:
        patient data: name of the disease with the probability of occurrence
        the result of treatment calculated below
    Return:
        final score as a sum of all calculated numbers of the set
    """
    res = {}
    for disorder in disorders:
        cure_score = ncures.get(disorder)
        disorder_score = disorders[disorder]
        if not cure_score:
            cure_score = 0
        if not disorder_score:
            disorder_score = 0
        res[disorder] = cure_score * disorder_score
    final_score = sum(res.values())
    # print("f: " + str(final_score))
    # sys.exit(0)
    return final_score


def check_score(random_meds, disorders):
    """
    Calculates the result of treatment for each set together and each disease.
    For example, drug No. 1 weight score for Parkinson's * 10 + drug No. 2 weight score for Parkinson's * 10....
    Args:
        diseases in set of meds – medical products (which support the treatment of the list of given diseases - sets)
        recomedation score - calculated weighted rating for each product
    Return:
        final score as a result of treatment
    """
    cures_score = {}
    for med in random_meds:
        score = med[3]
        cures = eval(med[5])
        cures = cures
        for cure in cures:
            x = cures_score.get(cure)
            if not x:
                x = 0
            cures_score[cure] = x + (score * 10)
    final_score = compare_scores(cures_score, disorders)
    return final_score


def run_search(disorders, meds, no_products):
    """
    Assumes 10,000 iterations of random attempts
    Draws 4 medsy – products to test the result that they have score together
    Having drawn medsy, goes to the function above checking what is the score for these meds
    Args:
        meds
    Return:
        best_meds at the end, a set is selected, where the final_score is the largest
    """
    best_meds = []
    max_score = 0
    for a in range(0, 10000):
        mlen = len(meds)
        random_meds = []
        rr = []
        n = 0
        while n < no_products:
            r = random.randrange(0, mlen)
            if r not in rr:
                rr.append(r)
                n = n + 1
                random_meds.append(meds[r])
        final_score = check_score(random_meds, disorders)
        if final_score > max_score:
            max_score = final_score
            best_meds = {'score': max_score, 'meds': random_meds}
    return best_meds


def main():
    df1 = entry_data()
    entry_data2(df1)
    sys.exit(0)


if __name__ == '__main__':
    main()
