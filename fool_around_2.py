from googlesearch import search
import random
from datetime import date, timedelta

urlList = []

def createQuery(title, site, location="remote", time=""):
    timeRange = str(determineDate(time))
    query = " ".join([title, site, location, timeRange])
    return query

def searchGoogle(query):
    seconds = random.randrange(3, 10)
    results = search(query, sleep_interval=seconds)

    count = 0
    urls = []
    for result in results:
        print(count, result)
        count += 1
        if count > 100:
            break
        urls.append(result)
    return urls

def pullOneSiteFromGoogle(title, site, location="", time=""):
    query = createQuery(title, site, location, time)
    print("query created: " + query)
    googleResults = searchGoogle(query)
    print("these them google results:", googleResults)
    urlList.extend(googleResults)
    return 

def listOfJobs():
    jobsList = ["\"product manager\"", "\"software engineer\"", 
                "\"developer\"", "\"designer\""]
    return jobsList

def listOfSites():
    sitesList = ["site:greenhouse.io", 
                 "site:lever.co",
                 "site:ashbyhq.com",
                 "site:jobs.*",
                 "site:myworkdayjobs.com"]
    return sitesList

def determineDate(timeRange=""):
    toSubtract = ""
    if timeRange == "day":
        toSubtract = timedelta(days=1)
    elif timeRange == "week":
        toSubtract = timedelta(days=7)
    else: 
        toSubtract = timedelta(days=31)
    return date.today() - toSubtract

def main():
    # pullOneSiteFromGoogle("\"product%20manager\"", "site:jobs.*")
    # print(listOfJobs())
    # print(listOfSites())
    # print(createQuery("\"product manager\"", "greenhouse.io"))
    # print(createQuery("a", "b", "c"))
    # urlList.extend(searchGoogle("choose"))
    # print(urlList)
    return

main()
