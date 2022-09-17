import unittest
import Ex1
from CallForElevator import CallForElevator
from Elevator import Elevator
from Building import Building


class MyTestCase(unittest.TestCase):
    def test_Bulding(self):
        Building_test = {
            "_minFloor": -2,
            "_maxFloor": 10,
            "_elevators": [
                {
                    "_id": 0,
                    "_speed": 1.0,
                    "_minFloor": -2,
                    "_maxFloor": 10,
                    "_closeTime": 2.0,
                    "_openTime": 2.0,
                    "_startTime": 3.0,
                    "_stopTime": 3.0
                },
                {
                    "_id": 1,
                    "_speed": 2.0,
                    "_minFloor": -2,
                    "_maxFloor": 10,
                    "_closeTime": 2.0,
                    "_openTime": 2.0,
                    "_startTime": 3.0,
                    "_stopTime": 3.0
                }
            ]
        }
        b = Building(min_floor=Building_test["_minFloor"], max_floor=Building_test["_maxFloor"])
        # Creating the elevators in the building
        for i in Building_test['_elevators']:
            elev = Elevator(id=i['_id'], speed=i['_speed'], min_floor=i['_minFloor'], max_floor=i['_maxFloor'],
                            close_time=i['_closeTime'], open_time=i['_openTime'], start_time=i['_startTime'],
                            stop_time=i['_stopTime'])
            b.list_elevators.append(elev)

        self.assertEqual(b.min_floor, -2)
        self.assertEqual(b.max_floor, 10)
        self.assertEqual(len(b.list_elevators), 2)

    def test_Elevetar(self):
        Building_test = {
            "_minFloor": -2,
            "_maxFloor": 10,
            "_elevators": [
                {
                    "_id": 0,
                    "_speed": 1.0,
                    "_minFloor": -2,
                    "_maxFloor": 10,
                    "_closeTime": 2.0,
                    "_openTime": 2.0,
                    "_startTime": 3.0,
                    "_stopTime": 3.0
                },
                {
                    "_id": 1,
                    "_speed": 2.0,
                    "_minFloor": -2,
                    "_maxFloor": 10,
                    "_closeTime": 2.0,
                    "_openTime": 2.0,
                    "_startTime": 3.0,
                    "_stopTime": 3.0
                }
            ]
        }
        b = Building(min_floor=Building_test["_minFloor"], max_floor=Building_test["_maxFloor"])
        # Creating the elevators in the building
        for i in Building_test['_elevators']:
            elev = Elevator(id=i['_id'], speed=i['_speed'], min_floor=i['_minFloor'], max_floor=i['_maxFloor'],
                            close_time=i['_closeTime'], open_time=i['_openTime'], start_time=i['_startTime'],
                            stop_time=i['_stopTime'])
            b.list_elevators.append(elev)

        self.assertEqual(b.list_elevators[0].min_floor, -2)
        self.assertEqual(b.list_elevators[0].max_floor, 10)

    def test_allocate_calls(self):
        Building_test = {
            "_minFloor": -2,
            "_maxFloor": 10,
            "_elevators": [
                {
                    "_id": 0,
                    "_speed": 1.0,
                    "_minFloor": -2,
                    "_maxFloor": 10,
                    "_closeTime": 2.0,
                    "_openTime": 2.0,
                    "_startTime": 3.0,
                    "_stopTime": 3.0
                },
                {
                    "_id": 1,
                    "_speed": 2.0,
                    "_minFloor": -2,
                    "_maxFloor": 10,
                    "_closeTime": 2.0,
                    "_openTime": 2.0,
                    "_startTime": 3.0,
                    "_stopTime": 3.0
                }
            ]
        }
        b = Building(min_floor=Building_test["_minFloor"], max_floor=Building_test["_maxFloor"])
        # Creating the elevators in the building
        for i in Building_test['_elevators']:
            elev = Elevator(id=i['_id'], speed=i['_speed'], min_floor=i['_minFloor'], max_floor=i['_maxFloor'],
                            close_time=i['_closeTime'], open_time=i['_openTime'], start_time=i['_startTime'],
                            stop_time=i['_stopTime'])
            b.list_elevators.append(elev)

        c= CallForElevator(4.37472729,0,-1,1)
        c1 = CallForElevator(16.95788289, -1, 0, 2)
        c2 = CallForElevator(22.0940563, 0, -1, 3)
        c3 = CallForElevator(85.52096662, 3, 2, 4)
        calls=[c,c1,c2,c3]
        Ex1.allocate(calls,b,'out.csv')
        self.assertEqual(c1.src, -1)
        self.assertEqual(c.src, 0)
        self.assertEqual(c2.dst, -1)
        self.assertEqual(c.data[5], 0)
        self.assertEqual(c1.data[5], 0)
        self.assertEqual(c2.data[5], 1)
        self.assertEqual(c3.data[5], 1)

  #  def test_something(self):
     #   self.assertEqual(Ex1., False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
