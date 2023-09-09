from kavenegar import *


class Kavenegar_Engine():
    sender_number = ''

    status_map = {1: 1, 2: 1, 4: 2, 5: 2, 6: 4, 10: 3, 11: 4, 13: 4, 14: 4, 100: 4}

    def __init__(self, api_key, sender_number):
        self.sender_number = sender_number
        self.api = KavenegarAPI(api_key)


    def send_sms(self, phone_number, message):
        '''
        ارسال پیامک
        :param phone_number: شماره تلفن مقصد
        :param message: پیغام مورد نظر
        :return:
        '''
        params = {
            'receptor': phone_number,
            'message': message,
            'sender': self.sender_number,
        }
        result = self.api.sms_send(params)
        if len(result) > 0:
            status = self.status_map[result[0]['status']]
            status_text = result[0]['statustext']
            cost = result[0]['cost']
            sent_at = result[0]['date']
            unique_message_id = result[0]['messageid']
            return {'status': status, 'status_text': status_text
                , 'cost': cost, 'sent_at': sent_at, 'unique_message_id': unique_message_id}
        else:
            return None

    def send_by_template(self, phone_number, template, params):
        args = {
            'receptor': phone_number,
            'template': template,
            'type': 'sms'}
        args.update(params)
        result = self.api.verify_lookup(args)
        if len(result) > 0:
            status = self.status_map[result[0]['status']]
            status_text = result[0]['statustext']
            cost = result[0]['cost']
            sent_at = result[0]['date']
            unique_message_id = result[0]['messageid']
            return {'status': status, 'status_text': status_text
                , 'cost': cost, 'sent_at': sent_at, 'unique_message_id': unique_message_id}
        else:
            return None

    def get_status(self, message_ids):
        params = {
            'messageid': message_ids
        }
        result = self.api.sms_status(params)
        states = [{'messageid': int(x['messageid']), 'status': self.status_map[x['status']], 'statustext': x['statustext']}
                  if x['status'] in self.status_map.keys()
                  else {'messageid': x['messageid'], 'status': 0, 'statustext': x['statustext']}
                  for x in result]
        return states
