import csv
import json
import sys

from Building import Building
from Elevator import Elevator
from CallForElevator import CallForElevator


def allocate(call_list: CallForElevator, b: Building, output):
    # time the person enter the elevator
    on_board = 0
    # end of call time
    end_time = 0
    # save the best elevator
    best_elv = -1
    # for every call in the call list
    for i in call_list:
        min_time = sys.float_info.max
        # for every elevator in the building
        for j in b.list_elevators:
            # for the current elevator check the time to the call
            if time_check(i, j) < min_time:
                best_elv = j.id
                min_time = time_check(i, j)
                on_board = int(min_time)+1
                end_time = on_board + call_time(i, j)
        # data i want to write in the csv
        i.data[5] = best_elv
        i.data[7] = on_board
        i.data[8] = end_time
        # added call to the elevator call list
        b.list_elevators[best_elv].calls.append(i)
        # write in the csv

    out_file = open(output, "w", newline="")
    writer = csv.writer(out_file)
    for i in call_list:
        writer.writerow(i.data)
    out_file.close()


def time_check(call: CallForElevator, elev: Elevator):
    if not elev.calls:
        if call.src == 0:
            return call.call_time
        return call.call_time + elev.close_time + elev.start_time + (
            abs(0 - call.src)) / elev.speed + elev.stop_time + elev.open_time
    else:
        if elev.calls[-1].data[8] > call.call_time:
            return elev.calls[-1].data[8] + elev.close_time + elev.start_time + (
                abs(elev.calls[-1].data[3] - call.src)) / elev.speed + elev.stop_time + elev.open_time
        else:
            if elev.calls[-1].data[3] == call.src:
                return call.call_time
            return call.call_time + elev.close_time + elev.start_time + (
                abs(elev.calls[-1].data[3] - call.src)) / elev.speed + elev.stop_time + elev.open_time


def call_time(call: CallForElevator, elev: Elevator):
    return elev.close_time + elev.start_time + (abs(call.dst - call.src)) / elev.speed + elev.stop_time + elev.open_time


def ex1(bld, calls, output):
    # Opening json file
    f = open(bld)
    data = json.load(f)
    # Creating a Building. Extracted from the json file
    b = Building(min_floor=data["_minFloor"], max_floor=data["_maxFloor"])
    # Creating the elevators in the building
    for i in data['_elevators']:
        elev = Elevator(id=i['_id'], speed=i['_speed'], min_floor=i['_minFloor'], max_floor=i['_maxFloor'],
                        close_time=i['_closeTime'], open_time=i['_openTime'], start_time=i['_startTime'],
                        stop_time=i['_stopTime'])
        b.list_elevators.append(elev)
    # Closing the json file
    f.close()
    # Opening CSV file
    c = open(calls)
    csv_reader = csv.reader(c)
    # Creating the callForElevators objects
    idx = 0
    call_list = []
    for row in csv_reader:
        call = CallForElevator(row[1], row[2], row[3], idx)
        idx = +1
        call_list.append(call)
    allocate(call_list, b, output)
    # Closing the CSV file
    c.close()


if __name__ == '__main__':
    input_list = sys.argv[1:]
    path_json = input_list[0]
    input = input_list[1]
    output_path = input_list[2]
    ex1(path_json, input, output_path)
