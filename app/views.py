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
            grouped[date] = []
        
        grouped[date].append(message["content"])

    # join into single string
    for key in grouped:
        grouped[key] = ". ".join(grouped[key])
    
    return grouped    

def group_by_day_list(messages):
    grouped = group_by_day(messages)
    
    return [ {
        "date": key,
        "content": grouped[key]
    }  for key in grouped.keys()]

# main function - must return as specified here
def events(request, is_testing=False):
    #messages = parse_messenger()

    events = [
        {
            "date": "2020-07-08",
            "content": "Hi filip"
        }
    ]
    return JsonResponse(events, safe=False)

    messages = parse_messenger()
    grouped_list = group_by_day_list(messages)

     # Object of automatic summarization.
    auto_abstractor = AutoAbstractor()
    # Set tokenizer.
    auto_abstractor.tokenizable_doc = SimpleTokenizer()
    # Set delimiter for making a list of sentence.
    auto_abstractor.delimiter_list = [".", "\n"]
    # Object of abstracting and filtering document.
    abstractable_doc = TopNRankAbstractor()
    # Summarize document.

    summaries = []

    for daily_message in grouped_list:
        result_dict = auto_abstractor.summarize(daily_message["content"], abstractable_doc)
        
        daily_summary = "".join(result_dict["summarize_result"])
        summaries.append(daily_summary)
    if not is_testing:
        return JsonResponse(grouped_list, safe=False)
    else:
        return render(request, 'example.html' ,{
            "data": zip(grouped_list, summaries)
        })

def test_events(request):
    return events(request, True)