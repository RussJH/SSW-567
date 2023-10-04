"""
Author: Russ Harrington
"""


import unittest
import json

from GitHubApi import PrintUserCommitsCountsPerRepo
from GitHubApi import GetListOfRepos
from GitHubApi import GetRepoCommitCounts
from GitHubApi import GetGithubCommitsFromRepo
from GitHubApi import GetGithubUserRepositoryList


def is_json(myjson):
    """Helper function to determine valid json
    """
    try:
        json.dumps(myjson)
    except ValueError as e:
        return False
    return True

class TestGitHubApi(unittest.TestCase):

    def testGetUserRepositoryInfo(self):
        """
        Test a valid user returns 
        """
        self.assertGreaterEqual(len(PrintUserCommitsCountsPerRepo("RussJH")), 1)
    
    def testGetUserRepositoryInfoInvalidUser(self):
        """
        Invalid user data should return an empty string
        """
        self.assertEqual(len(PrintUserCommitsCountsPerRepo("")), 0)

    def testGetListOfRepos(self):
        """
        """
        # test repos
        json_data = json.loads('[{\"name\": \"repo1\"},{\"name\": \"repo2\"},{\"name\": \"repo3\"}]')
        repo_list = ['repo1','repo2', 'repo3']
        self.assertEqual(GetListOfRepos(json_data), repo_list)
    
    def testGetListOfReposEmptySet(self):
        # test empty set
        json_data = json.loads('[]')
        self.assertEqual(GetListOfRepos(json_data), [])

    def testGetListOfReposInvalidJson(self):
        # test invalid json
        self.assertEqual(GetListOfRepos("String data"), [])

    def testRepoCommitCounts(self):
        # test valid
        json_data = json.loads('[ {\"sha\" : \"888fff\", \"commit\":{ \"comment_count\" : 0} },{\"sha\" : \"888fff\", \"commit\":{ \"comment_count\" : 0}}]')
        self.assertEqual(GetRepoCommitCounts(json_data), 2)

    def testRepoCommitCountsZero(self):
        # test empty set
        json_data = json.loads('[]')
        self.assertEqual(GetRepoCommitCounts(json_data), 0)

    def testRepoCommitCountsInvalid(self):
        # test invalid json
        self.assertEqual(GetRepoCommitCounts("INVALID JSON"), 0)

    def testGetGithubUserRepositoryList(self):
        #test valid json return
        self.assertTrue(is_json(GetGithubUserRepositoryList("RussJH")))
    
    def testGetGithubUserRepositoryListInvalid(self):
        #test valid json return
        self.assertTrue(is_json(GetGithubUserRepositoryList("")))

    def testGetGithubCommitsFromRepo(self):
        #test valid json data
        self.assertTrue(is_json(GetGithubCommitsFromRepo("RussJH","SSW-567")))

    def testGetGithubCommitsFromRepoInvalid(self):
        #test valid json data
        self.assertTrue(is_json(GetGithubCommitsFromRepo("RussJH","NOT_MY_REPO")))