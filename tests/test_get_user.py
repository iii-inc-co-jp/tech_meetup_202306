from service import Service


def test_get_user():
    target = Service()
    user = target.get_user('001')
    assert user['user_id'] == '001'
    assert user['name'] == 'テスト　１'
    assert user['age'] == 25

def test_get_user2():
    target = Service()
    user = target.get_user('002')
    assert user['user_id'] == '002'
    assert user['name'] == 'テスト　２'
    assert user['age'] == 32

def test_get_user3():
    target = Service()
    user = target.get_user('003')
    assert user['user_id'] == '003'
    assert user['name'] == 'テスト　３'
    assert user['age'] == 15
