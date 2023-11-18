def mlmm_program_solution(inputs):
    result = {'answer': []}
    for i in range(len(inputs)):
        cutoff = int(inputs[i][0])
        scores = inputs[i][2].split()
        scores = [int(num) for num in scores]
        num_scores = len(scores)
        max_bow = count_bow(scores, num_scores, cutoff)
        result['answer'].append(max_bow)
    return result


def count_bow(scores, num_scores, cutoff):
    count = 0
    for i in range(0, num_scores):
        summation = 0
        for j in range(i, num_scores):
            # If sum is less than k
            # then update sum and 
            # increment count
            if summation + scores[j] < cutoff:
                summation = scores[j] + summation
                count += 1
            else:
                break
    return count
