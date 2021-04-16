import copy


class FragileDict:
    def __init__(self, data=None):
        self._data = {}
        self._lock = True

        if data:
            self._data = copy.deepcopy(data)

    def __getitem__(self, key):
        if self._lock:
            return copy.copy(self._data[key])
        self._keys_to_copy.append(key)
        return self._data[key]

    def __setitem__(self, key, value):
        if self._lock:
            raise RuntimeError("Protected state")
        self._keys_to_copy.append(key)
        self._data[key] = value

    def __delitem__(self, key):
        if self._lock:
            raise RuntimeError("Protected state")
        del self._data[key]

    def __enter__(self):
        self._lock = False
        self._dir = set(dir(self))
        self._data_copy = copy.deepcopy(self._data)
        self._keys_to_copy = []
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type:
            print("Exception has been suppressed.")
            self._data = copy.deepcopy(self._data_copy)
        else:
            for key in self._keys_to_copy:
                self._data[key] = copy.deepcopy(self._data[key])

        dirs = set(dir(self)) ^ self._dir
        for attr in dirs:
            delattr(self, attr)

        self._lock = True
        return True

    def __contains__(self, key):
        return key in self._data


if __name__ == '__main__':

    # Test 1
    d = FragileDict({'key': 5})
    with d:
        d['key'] = 6
        d['ord'] = 7

    assert d['key'] == 6
    assert d['ord'] == 7

    # Test 2
    d = FragileDict({'key': 5})

    try:
        d['key'] = 6
        assert "RuntimeError" == ""
    except RuntimeError as e:
        pass

    try:
        d['ord'] = 7
        assert "RuntimeError" == ""
    except RuntimeError as e:
        pass

    assert d['key'] == 5
    assert 'ord' not in d

    # Test 3
    d = FragileDict({'key': 5})

    with d:
        d['key'] = 6
        assert d['key'] == 6
        d['ord'] = 7
        assert 'ord' in d and d['ord'] == 7
        raise Exception()

    assert d['key'] == 5
    assert 'ord' not in d

    # Test 4
    d = FragileDict({'key': []})

    with d:
        a = d['key']
        d['key'].append(10)
        a.append(10)

    a.append(10)
    assert a == [10, 10, 10]
    assert d['key'] == [10, 10]

    # Test 5
    d = FragileDict({'key': []})

    a = d['key']

    a.append(10)
    assert a == [10]
    assert d['key'] == []
