"""
Author: Russ Harrington
"""


import unittest
import json

from GitHubApi import GetUserRepositoryInfo
from GitHubApi import GetListOfRepos
from GitHubApi import GetRepoCommitCounts

class TestGitHubApi(unittest.TestCase):

    def testGetUserRepositoryInfo(self):
        """
        Test a valid user returns 
        """
        self.assertGreaterEqual(len(GetUserRepositoryInfo("RussJH")), 1)
    
    def testGetUserRepositoryInfoInvalidUser(self):
        """
        Invalid user data should return an empty string
        """
        self.assertEqual(len(GetUserRepositoryInfo("")), 0)

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