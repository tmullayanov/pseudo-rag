from filereader import read_from_file
from simple_rag import find_most_relevant, GroqClient


def read_ideas_knowledge_base(path: str) -> list[str]:
    contents = read_from_file(path)

    return contents.split()

def groq_llm_rag():
    user_prompt = input("What do you feel like doing? What would you like to experience?")
    ideas = read_ideas_knowledge_base('data/ideas.txt')
    
    relevant_document = find_most_relevant(user_prompt, ideas)

    # don't forget to set GROQ_API_KEY in environment!
    groq = GroqClient()

    sys_prompt_template = read_from_file('data/system_prompt.txt')
    groq.set_system_prompt_template(sys_prompt_template)
    
    response = groq.prompt(user_prompt, relevant_document)
    print(response)


if __name__ == "__main__":
    groq_llm_rag()
