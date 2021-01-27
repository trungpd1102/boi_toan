from flask import Blueprint, request, render_template, jsonify

boi_toan = Blueprint("boitoan", __name__)


@boi_toan.route('/boitoan/', methods=('GET', 'POST'))
def boi_toan_():
    # print(request.form)
    if request.method == 'POST':
        if 'ngu_hanh' in request.json:
            ret = _post_boi_toan(request)
            return ret
            # return render_template('result_ngu_hanh.html', man_can_chi=ret['man_can_chi'], man_menh=ret['man_menh'],
            #                        woman_can_chi=ret['woman_can_chi'], woman_menh=ret['woman_menh'])
        elif 'hop_tuoi' in request.json:
            ret = _post_boi_toan(request)
            return render_template('result_hop_tuoi.html', man_menh=ret['man_menh'], woman_menh=ret['woman_menh'],
                                   hop_tuoi=ret['hop_tuoi'])
    elif request.method == 'GET':
        return render_template("index.html")


# Dat ten Function noi bo :_name(protect), __(private)
def _post_boi_toan(req):
    # Nhận thông tin năm và xử lý
    # Query parameter
    # Front-end gửi về {"nam": 1998}
    body = req.json
    print(body) 
    year_of_man = str(body.get('man_menh'))
    print(year_of_man)
    year_of_woman = str(body.get('woman_menh'))

    man_can_chi = _calc_thien_can(year_of_man) + ' ' + _calc_dia_chi(year_of_man)
    man_menh = _calc_menh(_calc_thien_can(year_of_man), _calc_dia_chi(year_of_man))

    woman_can_chi = _calc_thien_can(year_of_woman) + ' ' + _calc_dia_chi(year_of_woman)
    woman_menh = _calc_menh(_calc_thien_can(year_of_woman), _calc_dia_chi(year_of_woman))

    hop_tuoi = _check_hop_tuoi(man_menh, woman_menh)
    # print(man_can_chi, man_menh, woman_can_chi, woman_menh, hop_tuoi)

    res = {
        'man_can_chi': man_can_chi,
        'man_menh': man_menh,
        'woman_can_chi': woman_can_chi,
        'woman_menh': woman_menh,
        'hop_tuoi': hop_tuoi
    }
    
    return res

def _get_boi_toan():
    return 'OK'


# Tinh ngũ hành tham khảo https://phongthuyhomang.vn/cach-tinh-thien-can-dia-chi-va-ngu-hanh-nam-sinh-cuc-nhanh/
def _calc_thien_can(year):
    """
    Tính toán thiên can theo năm sinh
    :param year: (str) năm
    :return: thien_can
    """

    if type(year) not in (str, ):
        raise ValueError("year() is not string".format(year))

    list_thien_can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỉ']
    num_thien_can = int(year[-1])
    thien_can = None

    # Duyệt list với index(can) tương ứng với num_thien_can
    for can in list_thien_can:
        if list_thien_can.index(can) == num_thien_can:
            thien_can = can

    return thien_can


def _calc_dia_chi(year):
    """
    Tính Địa chi theo năm sinh
    :param year: (str) năm
    :return: dia_chi
    """
    if type(year) not in (str, ):
        raise ValueError("year() is not string".format(year))

    #
    NUM = 12
    list_dia_chi = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi']
    num_dia_chi = int(year) % NUM
    dia_chi = None

    for chi in list_dia_chi:
        if list_dia_chi.index(chi) == num_dia_chi:
            dia_chi = chi

    return dia_chi


def _calc_menh(can, chi):
    """
    Cách tính cung mệnh ngũ hành theo can chi đã tính
    :param can: (str) Căn
    :param chi: (str) Chi
    :return: menh (str) Mệnh
    """
    if type(can) not in (str, ):
        raise ValueError("can() is not string".format(can))
    if type(chi) not in (str, ):
        raise ValueError("chi() is not string".format(chi))

    # Định nghĩa các số tương ứng với từng Căn
    dic_num_can = {
        'Giáp': 1,
        'Ất': 1,
        'Bính': 2,
        'Đinh': 2,
        'Mậu': 3,
        'Kỉ': 3,
        'Canh': 4,
        'Tân': 4,
        'Nhâm': 5,
        'Quý': 5
    }

    # Định nghĩa các số tương ứng với từng Chi
    dic_num_chi = {
        'Tý': 0,
        'Sửu': 0,
        'Ngọ': 0,
        'Mùi': 0,
        'Dần': 1,
        'Mão': 1,
        'Thân': 1,
        'Dậu': 1,
        'Thìn': 2,
        'Tị': 2,
        'Tuất': 2,
        'Hợi': 2
    }

    # Định nghĩa các số tương ứng với từng Hành
    dic_menh = {
        1: 'Kim',
        2: 'Thủy',
        3:  'Hỏa',
        4: 'Thổ',
        0: 'Mộc'
    }

    _num_can = dic_num_can.get(can)
    _num_chi = dic_num_chi.get(chi)

    NUM_M = 5
    _num_menh = (_num_can + _num_chi) % NUM_M
    menh = dic_menh.get(_num_menh)

    return menh


def _check_hop_tuoi(man_menh, woman_menh):
    """
    Xem tuôi 2 người có hợp, khắc, bình thường
    :param man_menh: (str) Mệnh của nam
    :param woman_menh: (str) Mệnh của nữ
    :return:  result(str) Kết quả: (Hợp, Khắc, Bình thường)
    """
    if type(man_menh) not in (str, ):
        raise ValueError("man_menh() is not string".format(man_menh))
    if type(woman_menh) not in (str, ):
        raise ValueError("woman_menh() is not string".format(woman_menh))

    # Các cặp mệnh tương sinh
    _tup_tuong_sinh = (
        ('Mộc', 'Hỏa'),
        ('Hỏa', 'Thổ'),
        ('Thổ', 'Kim'),
        ('Kim', 'Thủy'),
        ('Thủy', 'Mộc')
    )

    # Các cặp mệnh tương khắc
    _tup_tuong_khac = (
        ('Thủy', 'Hỏa'),
        ('Hỏa', 'Kim'),
        ('Kim', 'Mộc'),
        ('Mộc', 'Thổ'),
        ('Thổ', 'Thủy')
    )

    _menh_man_woman_asc = (man_menh, woman_menh)
    _menh_man_woman_desc = (woman_menh, man_menh)

    if (_menh_man_woman_asc in _tup_tuong_sinh) or (_menh_man_woman_desc in _tup_tuong_sinh) is True:
        result = 'Tương Sinh - Hợp'
    elif (_menh_man_woman_asc in _tup_tuong_khac) or (_menh_man_woman_desc in _tup_tuong_khac) is True:
        result = 'Tương Khắc - Không hợp'
    else:
        result = 'Bình Thường'

    return result
