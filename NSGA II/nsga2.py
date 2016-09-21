import numpy as np
import matplotlib.pyplot as plt


class NSGA2_Class(object):
    @staticmethod
    def start():

        opt = NSGA2_Class()
        opt.run_NSGA2()

    def run_NSGA2(self):

        print("\n\nNSGA2 simulation started...")
        obj_cnt = 2
        sol_cnt = 30
        Matrix = np.random.randint(10, 1000, [obj_cnt, sol_cnt])
        sols = []
        for cnt in range(sol_cnt):
            sol_i = element(Matrix[:, cnt])
            sols.append(sol_i)

        F_list = [[]]
        for sol_p in sols:
            sol_p.S_list = []
            sol_p.n_val = 0
            for sol_q in sols:
                if sol_p_dominates_q(sol_p.objective, sol_q.objective):
                    sol_p.S_list.append(sol_q)
                elif sol_p_dominates_q(sol_q.objective, sol_p.objective):
                    sol_p.n_val += 1
            if sol_p.n_val == 0:
                sol_p.rank = 1
                F_list[-1].append(sol_p)
        pass
        i_val = 1
        while True:
            Q_list = []
            for sol_p in F_list[i_val-1]:
                for sol_q in sol_p.S_list:
                    sol_q.n_val -= 1
                    if sol_q.n_val == 0:
                        sol_q.rank = i_val + 1
                        Q_list.append(sol_q)
            i_val += 1
            if len(Q_list) == 0:
                break
            F_list.append(Q_list)
        pass
        pareto_front = []
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for F_i in F_list:
            temp_list = []
            for F_ij in F_i:
                temp_list.append(F_ij.objective)
            temp_list = np.array(temp_list)
            temp_list = temp_list[np.argsort(temp_list[:, 0])]
            plt.plot(temp_list[:, 0], temp_list[:, 1])
            for i, j in zip(temp_list[:, 0], temp_list[:, 1]):
                ax.annotate(str(i)+str(',')+str(j), xy=(i, j))
            pareto_front.append(temp_list)





        plt.plot(Matrix[0, :], Matrix[1, :], "o")
        plt.show()
        pass


class element(object):

    def __init__(self, objective):

        self.objective = objective
        self.S_list = []
        self.n_val = None
        self.rank = None


def sol_p_dominates_q(p_obj, q_obj):

    if p_obj[0] < q_obj[0] and p_obj[1] < q_obj[1]:
        return True
    return False




def main():

    NSGA2_Class.start()

if __name__ == '__main__':
    main()
