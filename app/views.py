from json.decoder import JSONDecodeError
from django.conf import settings
from django.http.response import JsonResponse
from app.parser import format_grouped_messages, group_by_day, group_by_day_list, parse_all, parse_messenger
from django.shortcuts import render
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
from django.http import HttpResponse

from datetime import datetime

def ping(request):
    return HttpResponse("pong")

# main function - must return as specified here
def events(request, is_testing=False):
    date_from = request.GET.get('dateFrom',None)
    date_to = request.GET.get('dateTo',None)

    if not settings.DEBUG:
        summaries = [
            {
                "date": "18. June, 2020",
                "content": "I really liked the party Andy organised yesterday. It was a blast!"
            },
            {
                "date": "19. June, 2020",
                "content": "Have you started to study for the exam next week yet? I heard its one of the most difficult exams this year."
            },
            {
                "date": "20. June, 2020",
                "content": "Hey have you heard from Ana, i heard she broke her arm last week while skating. Hope shes doing okay"
            },
            {
                "date": "21. June, 2020",
                "content": "Are you coming to the seminar tomorrow morning? I heard that attendance is mandatory and if you don't come you lose the right to attend exam."
            }
        ]
    else:
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

        
        if not is_testing:
            if date_from and date_to:
                date_from = datetime.strptime(date_from, '%Y-%m-%d')
                date_to = datetime.strptime(date_to, '%Y-%m-%d')
                grouped_list = list(filter(lambda x: date_from <= x["date"] <= date_to, grouped_list))

            grouped_list = format_grouped_messages(grouped_list, "%b %d %Y")

            for daily_message in grouped_list:
                result_dict = auto_abstractor.summarize(daily_message["content"], abstractable_doc)
                
                daily_summary = "".join(result_dict["summarize_result"])
                summaries.append(daily_summary)


    return JsonResponse(summaries, safe=False)
    # for daily_message in grouped_list:
    #     result_dict = auto_abstractor.summarize(daily_message["content"], abstractable_doc)
        
    #     daily_summary = "".join(result_dict["summarize_result"])
    #     summaries.append(daily_summary)

    # return render(request, 'example.html' ,{
    #     "data": zip(grouped_list, summaries)
    # })

def graph_points(request):

    f = open('tocke.txt', 'r')
    lines = f.readlines()
    
    all_points = []
    for line in lines:
        point = float(line.replace(',',''))
        all_points.append(point)

    return JsonResponse(all_points, safe=False)


def test_events(request):
    return events(request, True)


