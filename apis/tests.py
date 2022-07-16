from django.test import TestCase
from .models import StudentModel

# Create your tests here.


class NewStudentTest(TestCase):
    def test_can_save_a_POST_request(self):
        response = self.client.post(
            path="/api/student/",
            data={
                "studentId": "asectyler4a10b",
                "name": "Tyler Matther",
                "phone": 9991327884,
                "gender": "M",
                "father": "Burton Maldonado",
                "mother": "Misty Gardner",
                "address": "Bloomington, Mali",
                "group": "D",
                "age": 3,
                "dob": "2017/7/20",
                "speechTherapy": 4000,
                "therapy": 0,
                "transportation": 0,
                "tuition": 8000,
                "snacks": 0,
                "isAdmission": True,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(StudentModel.objects.count(), 1)
        new_student = StudentModel.objects.first()
        self.assertEqual(new_student.studentId, "asectyler4a10b")

    def test_can_handle_GET_request(self):
        testStudentId = "asectyler4a10b"
        testAddress = "Bloomington, Mali"

        response = self.client.post(
            "/api/student/",
            data={
                "studentId": testStudentId,
                "name": "Tyler Matther",
                "phone": 9991327884,
                "gender": "M",
                "father": "Burton Maldonado",
                "mother": "Misty Gardner",
                "address": testAddress,
                "group": "D",
                "age": 3,
                "dob": "2017/7/20",
                "speechTherapy": 4000,
                "therapy": 0,
                "transportation": 0,
                "tuition": 8000,
                "snacks": 0,
                "isAdmission": True,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(StudentModel.objects.count(), 1)
        new_student = self.client.get("/api/student/details/" + testStudentId).json()

        self.assertEqual(new_student["studentId"], testStudentId)
        self.assertEqual(new_student["address"], testAddress)

    def test_can_update_data(self):
        testStudentId = "asectyler4a10b"
        testAddress = "Bloomington, Mali"
        self.client.post(
            "/api/student/",
            data={
                "studentId": testStudentId,
                "name": "Tyler Matther",
                "phone": 9991327884,
                "gender": "M",
                "father": "Burton Maldonado",
                "mother": "Misty Gardner",
                "address": testAddress,
                "group": "D",
                "age": 3,
                "dob": "2017/7/20",
                "speechTherapy": 4000,
                "therapy": 0,
                "transportation": 0,
                "tuition": 8000,
                "snacks": 0,
                "isAdmission": True,
            },
            content_type="application/json",
        )
        self.client.put(
            "/api/student/details/" + testStudentId,
            data={
                "studentId": testStudentId,
                "name": "Tyler Matthew",
                "phone": 9991327884,
                "gender": "M",
                "father": "Burton Maldonado",
                "mother": "Misty Gardner",
                "address": testAddress,
                "group": "D",
                "age": 3,
                "dob": "2017/7/20",
                "speechTherapy": 4000,
                "therapy": 0,
                "transportation": 0,
                "tuition": 8000,
                "snacks": 0,
                "isAdmission": True,
            },
            content_type="application/json",
        )
        response = self.client.get("/api/student/details/" + testStudentId)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(StudentModel.objects.count(), 1)
        changed_record = response.json()
        self.assertEqual(changed_record["name"], "Tyler Matthew")
        self.assertEqual(changed_record["gender"], "M")
