"""
Author: Russ Harrington
Date: 2023-10-02
Assignment HW-04a - Develop with the Perspective of the Tester in mind    
    For this assignment imagine that you have been asked to develop a function that will interface with GitHub 
    in order to extract and present useful information to your user. The function will communicate using 
    the RESTful services APIs provided by GitHub. The GitHub APIs will allow you to query for information about 
    users, repositories, etc... which can be retrieved using the function, and then be displayed in the application.

    What should make this assignment different from other programming assignments is in how you will approach it. 
    You should approach this assignment as a developer who more than anything else has the perspective of the tester in the front of your mind. 

    The developer looks at the requirements and asks how should I design and implement this function, 
    but the tester will ask questions such as what will I need to test for in this function?  And how will I test this function?   
    As you design and write the function as a developer, you should consider the perspective of the tester in any of your design and implementation decisions.
    One deliverable of this assignment will be to reflect and comment on this.
"""
import requests
import json

#Constants for GITHUB
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_API_REPO = 'repos'
GITHUB_API_USERS = 'users'
GITHUB_API_COMMITS = 'commits'


def GetListOfRepos(json_data):
    """Get the list of repositories from a github API return 
    Parameters
    ----------
    json_data : JSON
        A JSON object which is populated by the github API for getting repositories attached to a user

    Returns
    -------
    list
        A list of repository names
    """
    repos = []
    try:
        for gitItem in json_data:
            repos.append(gitItem['name'])
    except TypeError:
        print("Invalid JSON")
    return repos
    

def GetRepoCommitCounts(json_data):
    """Get the list of valid commits from a github API return 
    Parameters
    ----------
    json_data : JSON
        A JSON object which is populated by the github API for getting commits from a repo

    Returns
    -------
    integer
        an integer count of the number of commits in the supplied JSON data
    """
    repos = dict()
    commit_count = 0
    try:
        for commit in json_data:
            # only count commits if they are valid, meaning they have a sha
            if('sha' in commit):
                commit_count+=1            
    except TypeError as e:
        print("Invalid JSON")
    return commit_count

def GetGithubUserRepositoryList(userID):
    """Get repos for a user from the github API  
    Parameters
    ----------
    userID : String
        A name of a user in Github

    Returns
    -------
    json
        Response from Github in json 
    """
    json_data = json.loads('[]')
    request_url = "{}{}/{}/{}".format(GITHUB_API_URL, GITHUB_API_USERS, userID, GITHUB_API_REPO)
    response = requests.get(request_url)
    if(response.status_code == 200):
        json_data = json.loads(response.text)
    return json_data

def GetGithubCommitsFromRepo(userID, repoName):
    """Get commits from a github API return 
    Parameters
    ----------
    userID : String
        A name of a user in Github
    repoName : String
        A name of a repo in Github

    Returns
    -------
    json
        Response from Github in json 
    """
    json_data = json.loads('[]')
    commit_url = "{}{}/{}/{}/{}".format(GITHUB_API_URL, GITHUB_API_REPO, userID,  repoName, GITHUB_API_COMMITS )
    response = requests.get(commit_url)
    if(response.status_code == 200):
        json_data = json.loads(response.text)
    return json_data
        
def PrintUserCommitsCountsPerRepo(userID):
    """Get a list of repos and commit counts for a specified user 
    Parameters
    ----------
    userID : String
        A name of a user in Github

    Returns
    -------
    list
        A list of formatted strings in the form of: 
        Repo: xyz Number of Commits: abc
    """
    return_list = []
    
    json_data = GetGithubUserRepositoryList(userID)
    repos = dict.fromkeys(GetListOfRepos(json_data))
    
    for key in repos:
        json_data = GetGithubCommitsFromRepo(userID, key)
        repos[key] = GetRepoCommitCounts(json_data)

    for key in repos:
        return_list.append("Repo: {} Number of Commits: {}".format(key, repos[key]))
    return return_list


def main():
    """Main method"""
    retval = GetUserRepositoryInfo('RussJH')
    for str in retval:
        print(str)

if __name__ == '__main__':
    main()