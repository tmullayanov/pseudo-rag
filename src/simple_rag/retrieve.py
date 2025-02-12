def jaccard_similarity(query: str, document: str) -> float:
    """
    The Jaccard index is a statistic used for gauging the similarity and diversity of sample sets.
    More on the subject: https://en.wikipedia.org/wiki/Jaccard_index
    """
    query = query.lower().split(" ")
    document = document.lower().split(" ")

    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))

    return len(intersection) / len(union)


def find_most_relevant(user_input: str, corpus: list[str]):
    similarities = []
    for doc in corpus:
        similarity = jaccard_similarity(user_input, doc)
        similarities.append(similarity)

    return corpus[similarities.index(max(similarities))]
