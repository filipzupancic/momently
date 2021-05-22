from django.http.response import JsonResponse
from app.parser import parse_messenger
from django.shortcuts import render
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor


# Create your views here.

def group_by_day(messages):

    grouped = {}

    for message in messages:
        date = message["timestamp"].strftime('%d/%m/%y')

        if date not in grouped:
            grouped[message]
            pass

    #{ message["content"] :  for message in messages}


# main function - must return as specified here
def events(request):
    #messages = parse_messenger()

    events = [
        {
            "date": "2020-07-06",
            "content": "This is my recap"
        },
        {
            "date": "2020-07-07",
            "content": "This is my other recap"
        },
        {
            "date": "2020-07-08",
            "content": "Hi filip"
        }
    ]
    return JsonResponse(events, safe=False)

    



def sample_function(request):

    my_string = """
    The BBC still has questions to answer after an inquiry into Panorama's Diana interview, a senior Tory MP has said.

    The report found Martin Bashir used deception to get the 1995 scoop.

    Julian Knight, chairman of a committee that scrutinises the organisation, told the BBC he wanted to know why Bashir was rehired as a correspondent in 2016 and later promoted to religion editor.

    He has written to the BBC's director general Tim Davie ahead of a private committee meeting on Wednesday.

    Speaking on BBC Radio 4's Today programme, he questioned why Bashir was "good enough" to be re-employed by the BBC, if he had been found to lie and had had to resign from US news and chat network MSNBC in 2013 over controversial remarks.

    Mr Knight, chairman of the House of Commons Digital, Culture, Media and Sport Committee, added: "I would also want to know, what precisely did he do in his job? He wasn't on air a great deal."

    The BBC has defended rehiring Bashir, saying the post was filled after a competitive interview process. Bashir left the BBC earlier this month without a pay-off.

    What is the Diana interview row all about?
    Timeline of the controversy
    What next for the BBC?
    Mr Knight said the BBC should have an "open mind" about compensation for whistleblowers, such as graphic designer Matt Wiessler, who raised concerns about fake bank statements he produced for Bashir.

    And he questioned a proposal by former BBC chairman Lord Grade for a new editorial board - instead calling for editorial policy to be strengthened at the corporation.

    "I do wonder whether or not it will be a talking shop full of people with big salaries," he said.

    The independent inquiry by former senior judge Lord Dyson found Bashir was unreliable and dishonest, and that the corporation fell short of its high standards when answering questions about the 1995 interview.

    Since the report was published on Thursday, the Duke of Cambridge has blamed BBC failings for fuelling his mother's paranoia and worsening his parents' relationship. The Duke of Sussex has also spoken about the hurt caused by the interview.

    Broadcast in November 1995, the interview marked the first time a serving royal had spoken in such candid terms about life in the Royal Family or relationships with other royals. Shortly afterwards, the Queen wrote to Prince Charles and Princess Diana telling them to divorce.

    The princess died in 1997, after the car she was in crashed in the Pont de l'Alma tunnel, in Paris.

    Reacting to the inquiry findings, Prime Minister Boris Johnson said on Friday the BBC should take "every possible step to make sure nothing like this ever happens again". Ministers have suggested the BBC's governance might need reform.

    Next year will see a mid-term review of the corporation's royal charter - an agreement with the government over what the BBC intends to do, including how it is funded and run.

    But Newsnight's Nicholas Watt said the talk in Whitehall was that the charter review was just a health check and the current BBC board could be allowed to carry out the job of improving governance.

    The BBC has insisted it has made fundamental changes in governance since the 1990s.

    Speaking on BBC Radio 4's Today programme, the BBC's former chief operating officer Caroline Thomson, called for the introduction of a series of measures to restore trust "among BBC journalists and staff as well as among the public".

    Instead of an editorial board, she suggested the introduction of a new non-executive board member with dedicated responsibility for news and editorial matters who could be "the face of transparency" and available to those who would like to whistleblow.

    During Princess Diana's interview with Bashir for Panorama, the princess spoke about her unhappy marriage to Prince Charles, and famously said: "There were three of us in this marriage."

    The inquiry was commissioned by the BBC last year, after Earl Spencer - Diana's brother - went public with his concerns about the tactics used to get the interview.

    Ofcom - the media watchdog - said it would be talking to the BBC about what further action might be needed.
    """

    document = my_string

    # Object of automatic summarization.
    auto_abstractor = AutoAbstractor()
    # Set tokenizer.
    auto_abstractor.tokenizable_doc = SimpleTokenizer()
    # Set delimiter for making a list of sentence.
    auto_abstractor.delimiter_list = [".", "\n"]
    # Object of abstracting and filtering document.
    abstractable_doc = TopNRankAbstractor()
    # Summarize document.
    result_dict = auto_abstractor.summarize(document, abstractable_doc)


    # Output result.
    # for sentence in result_dict["summarize_result"]:
    #     print(sentence)

    parse_messenger()

    # JsonResponse()
    return render(request, 'example.html' ,{
        "original": document,
        "summary": "".join(result_dict["summarize_result"])
    })