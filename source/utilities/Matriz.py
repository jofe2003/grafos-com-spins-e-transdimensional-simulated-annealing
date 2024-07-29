class Matriz:

    def dot(self, x:list, w:list)->list:
        """matriz que multiplica o vetor x pela matriz w quando a matriz w está na sua forma de triângulação
        x: vetor
        w: matriz de pesos
        Returns:
            resultado multiplicado
        """
        sizeIn = len(x)
        sizeW = len(w)
        out = [0]
        k = 0
        for i in range(sizeIn): # do x e do w
            sizeWi = len(w[i])
            for j in range(sizeWi): # do w[i]
                out.append(0)
                out[k]+=w[i][j]*x[i]
                k+=1
            k-=1
            out.pop(-1) # remove o último elemento da lista
        return out

# x = [1, 2, 3, 4]
# w = [[1, 1/2], [1, 1], [1, 1], [1]]
# m = Matriz()
# saida = m.dot(x, w)
# print(saida)
