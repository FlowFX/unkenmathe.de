

class TestBasicViews:

    def test_home_page_GET(self, client):
        # GIVEN any state
        # WHEN calling the home page
        response = client.get('/')

        # THEN it's there
        assert response.status_code == 200


class TestExerciseModel:

    def test_exercise_can_be_saved(self, db):
        # GIVEN any state
        # WHEN adding a new exercise to the database
        # THEN it works
        pass
