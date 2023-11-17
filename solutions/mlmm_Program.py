def mlmm_program_solution():
    result = {'answer':[]}
    for i in range(len(input_data)):
        cutoff = int(input_data[i][0])
        scores = input_data[i][2].split()
        scores = [int(num) for num in scores]
        num_scores = len(scores)
        max_bow = count_bow(scores, num_scores, cutoff) 
        result['answer'].append(max_bow)
    return result

def count_bow(scores, num_scores, cutoff):
    count = 0
    for i in range(0, num_scores):
        sum = 0;
        for j in range(i, num_scores):
            # If sum is less than k
            # then update sum and 
            # increment count
            if (sum + scores[j] < cutoff):
                sum = scores[j] + sum
                count += 1
            else:
                break
    return count
