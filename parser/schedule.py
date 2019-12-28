import config
import requests

class ScheduleParser():
    def parse(self, params: dict, do_req: bool = True, l: list = []) -> list:
        if do_req:
            l = self.__get_data()
        
        param_name = list(params.keys())[0]
        param_value = params[param_name]
        del params[param_name]

        confs = []

        if param_name == 'speaker':
            for conference in l:
                for person in conference['persons']:
                    if person['public_name'].lower() == param_value.lower():
                        confs.append(conference)
                        break
                    
        elif param_name == 'room':
            for conference in l:
                if conference['room'].lower() == param_value.lower():
                    confs.append(conference)



        if len(list(params.keys())) > 0:
            return self.parse(params, False, confs)
        return confs

    def __get_data(self) -> list:
        resp = requests.get(config.SCHEDULE_URL)
        elements = []
        for day in resp.json()['schedule']['conference']['days']:
            for room in day['rooms']:
                for conference in day['rooms'][room]:
                    elements.append(conference)
        return elements

