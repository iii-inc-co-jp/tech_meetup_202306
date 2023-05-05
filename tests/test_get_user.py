from service import Service

def test_get_user():
    target = Service()
    user = target.get_user('001')
    assert user['user_id'] == '001'
    assert user['name'] == 'テスト　１'
    assert user['age'] == 25
