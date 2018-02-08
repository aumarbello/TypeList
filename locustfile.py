from locust import HttpLocust, TaskSet, task


class UserBehaviour(TaskSet):

    @task
    def get_tests(self):
        self.client.get("/tests")

    @task
    def put_test(self):
        self.client.post("/tests", {"name": "unit testing", "description": "checking the behaviour of a small unit of "
                                                                           "code in isolation"})


class WebsiteUser(HttpLocust):
    task_set = UserBehaviour

