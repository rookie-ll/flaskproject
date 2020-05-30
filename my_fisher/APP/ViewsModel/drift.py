from APP.webapp.libs.enums import PendingStatus


class DriftCollection:
    def __init__(self, drifts, current_user_id):
        self.data = []
        self.data.extend(self._parse(drifts, current_user_id))

    def _parse(self, drifts, current_user_id):
        return [DriftViewModel(drift, current_user_id) for drift in drifts]


class DriftViewModel:
    def __init__(self, drift, current_user_id):
        self.data = {}

        self.data = self._parse(drift, current_user_id)

    @staticmethod
    def requester_or_gifter(drift, current_user_id):
        if drift.requester_id == current_user_id:
            you_are = "requester"
        else:
            you_are = "gifter"
        return you_are

    def _parse(self, drift, current_user_id):
        you_are = DriftViewModel.requester_or_gifter(drift, current_user_id)
        pending_status = PendingStatus.pending_str(drift.pending, you_are)
        r = {
            'drift_id': drift.id,
            'you_are': you_are,
            'book_title': drift.book_title,
            'book_author': drift.book_author,
            'book_img': drift.book_img,
            'date': drift.create_datetime.strftime('%Y-%m-%d'),
            'operator': drift.requester_nickname if you_are != 'requester' else drift.gifter_nickname,
            'message': drift.message,
            'address': drift.address,
            'status_str': pending_status,
            'recipient_name': drift.recipient_name,
            'mobile': drift.mobile,
            'status': drift.pending
        }
        return r