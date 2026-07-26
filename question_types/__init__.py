REGISTRY = {}

def register(question):
    REGISTRY[question.__name__] = question.write
    return question

from . import arithmetic

if __name__ == "__main__":
    print(REGISTRY)
