class UnsortedTableMap:

    def __init__(self):
        self._table = []         

    # --------- auxiliar ---------
    def _buscar(self, k):
        for j in range(len(self._table)):
            if self._table[j][0] == k:
                return j
        return -1

    def __len__(self):
        # len(M)
        return len(self._table)

    def __getitem__(self, k):
        j = self._buscar(k)
        if j == -1:
            raise KeyError(k)
        return self._table[j][1]

    def __setitem__(self, k, v):
        j = self._buscar(k)
        if j != -1:
            self._table[j][1] = v  
        else:
            self._table.append([k, v])

    def __delitem__(self, k):
        j = self._buscar(k)
        if j == -1:
            raise KeyError(k)
        self._table.pop(j)

    def __contains__(self, k):
        return self._buscar(k) != -1

    def __iter__(self):
        for entrada in self._table:
            yield entrada[0]

    def __eq__(self, otro):
        if len(self) != len(otro):
            return False
        for k, v in self._table:
            if k not in otro or otro[k] != v:
                return False
        return True


    def __repr__(self):
        return '{' + ', '.join(f'{k!r}: {v!r}' for k, v in self._table) + '}'
