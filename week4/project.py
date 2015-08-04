"""
Project 4: Computing alignments of sequences
Need to implement four functions:

build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag)
compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
"""

def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    '''
    Takes as input a set of characters alphabet and three scores
    diag_score, off_diag_score, and dash_score. The function returns
    a dictionary of dictionaries whose entries are indexed by pairs of
    characters in alphabet plus '-'. The score for any entry indexed by
    one or more dashes is dash_score. The score for the remaining diagonal
    entries is diag_score. Finally, the score for the remaining off-diagonal
    entries is off_diag_score.
    '''
    result = {}
    alphabet_list = list(alphabet)
    alphabet_list.append("-")
    for idx_i in range(len(alphabet_list)):
        first_letter = alphabet_list[idx_i]
        result[first_letter] = {}
        for idx_j in range(len(alphabet_list)):
            second_letter = alphabet_list[idx_j]
            if first_letter == "-" or second_letter == "-":
                result[first_letter][second_letter] = dash_score
            elif first_letter == second_letter:
                result[first_letter][second_letter] = diag_score
            else:
                result[first_letter][second_letter] = off_diag_score
    return result

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    '''
    Takes as input two sequences seq_x and seq_y whose elements share a
    common alphabet with the scoring matrix scoring_matrix. The function
    computes and returns the alignment matrix for seq_x and seq_y as
    described in the Homework. If global_flag is True, each entry of the
    alignment matrix is computed using the method described in Question 8
    of the Homework. If global_flag is False, each entry is computed
    using the method described in Question 12 of the Homework.
    '''
    len_m = len(seq_x)
    len_n = len(seq_y)
    alignment_matrix = []
    for idx_i in range(len_m+1):
        alignment_matrix.append([0] * (len_n+1))
    
    for idx_i in range(1, len_m+1):
        alignment_matrix[idx_i][0] = alignment_matrix[idx_i-1][0] + scoring_matrix[seq_x[idx_i-1]]["-"]
        if not global_flag and alignment_matrix[idx_i][0] < 0:
            alignment_matrix[idx_i][0] = 0
    for idx_j in range(1, len_n+1):
        alignment_matrix[0][idx_j] = alignment_matrix[0][idx_j-1] + scoring_matrix["-"][seq_y[idx_j-1]]
        if not global_flag and alignment_matrix[0][idx_j] < 0:
            alignment_matrix[0][idx_j] = 0
    for idx_i in range(1, len_m+1):
        for idx_j in range(1, len_n+1):
            value_1 = alignment_matrix[idx_i-1][idx_j-1] + \
                      scoring_matrix[seq_x[idx_i-1]][seq_y[idx_j-1]]
            value_2 = alignment_matrix[idx_i-1][idx_j] + \
                      scoring_matrix[seq_x[idx_i-1]]["-"]
            value_3 = alignment_matrix[idx_i][idx_j-1] + \
                      scoring_matrix["-"][seq_y[idx_j-1]]
            alignment_matrix[idx_i][idx_j] = max(value_1, value_2, value_3)
            if not global_flag and alignment_matrix[idx_i][idx_j] < 0:
                alignment_matrix[idx_i][idx_j] = 0
    return alignment_matrix

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    '''
    Takes as input two sequences seq_x and seq_y whose elements share a 
    common alphabet with the scoring matrix scoring_matrix. This function 
    computes a global alignment of seq_x and seq_y using the global 
    alignment matrix alignment_matrix.

    The function returns a tuple of the form (score, align_x, align_y) 
    where score is the score of the global alignment align_x and align_y. 
    Note that align_x and align_y should have the same length and may 
    include the padding character '-'. 
    '''
    dummy_i = len(seq_x)
    dummy_j = len(seq_y)
    result_x = ""
    result_y = ""
    result_score = alignment_matrix[dummy_i][dummy_j]
    while dummy_i != 0 and dummy_j != 0:
        if alignment_matrix[dummy_i][dummy_j] == \
           alignment_matrix[dummy_i-1][dummy_j-1] + scoring_matrix[seq_x[dummy_i-1]][seq_y[dummy_j-1]]:
            result_x = seq_x[dummy_i-1] + result_x
            result_y = seq_y[dummy_j-1] + result_y
            dummy_i -= 1
            dummy_j -= 1
        else:
            if alignment_matrix[dummy_i][dummy_j] == \
               alignment_matrix[dummy_i-1][dummy_j] + scoring_matrix[seq_x[dummy_i-1]]["-"]:
                result_x = seq_x[dummy_i-1] + result_x
                result_y = "-" + result_y
                dummy_i -= 1
            else:
                result_x = "-" + result_x
                result_y = seq_y[dummy_j-1] + result_y
                dummy_j -= 1
    while dummy_i != 0:
        result_x = seq_x[dummy_i-1] + result_x
        result_y = "-" + result_y
        dummy_i -= 1
    while dummy_j !=0:
        result_x = "-" + result_x
        result_y = seq_y[dummy_j-1] + result_y
        dummy_j -= 1
    return (result_score, result_x, result_y)

def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    '''
    Takes as input two sequences seq_x and seq_y whose elements share a 
    common alphabet with the scoring matrix scoring_matrix. This function 
    computes a local alignment of seq_x and seq_y using the local alignment 
    matrix alignment_matrix.

    The function returns a tuple of the form (score, align_x, align_y) 
    where score is the score of the optimal local alignment align_x and 
    align_y. Note that align_x and align_y should have the same length 
    and may include the padding character '-'. 
    '''
    max_value = -1
    dummy_i = -1
    dummy_j = -1
    # get the max value of the alignment matrix and use that as starting point
    for idx_i in range(len(seq_x)+1):
        for idx_j in range(len(seq_y)+1):
            if alignment_matrix[idx_i][idx_j] > max_value:
                dummy_i = idx_i
                dummy_j = idx_j
                max_value = alignment_matrix[idx_i][idx_j]
    result_x = ""
    result_y = ""
    result_score = alignment_matrix[dummy_i][dummy_j]
    while dummy_i != 0 and dummy_j != 0 and alignment_matrix[dummy_i][dummy_j] !=0:
        if alignment_matrix[dummy_i][dummy_j] == \
           alignment_matrix[dummy_i-1][dummy_j-1] + scoring_matrix[seq_x[dummy_i-1]][seq_y[dummy_j-1]]:
            result_x = seq_x[dummy_i-1] + result_x
            result_y = seq_y[dummy_j-1] + result_y
            dummy_i -= 1
            dummy_j -= 1
        else:
            if alignment_matrix[dummy_i][dummy_j] == \
               alignment_matrix[dummy_i-1][dummy_j] + scoring_matrix[seq_x[dummy_i-1]]["-"]:
                result_x = seq_x[dummy_i-1] + result_x
                result_y = "-" + result_y
                dummy_i -= 1
            else:
                result_x = "-" + result_x
                result_y = seq_y[dummy_j-1] + result_y
                dummy_j -= 1
    while dummy_i != 0 and alignment_matrix[dummy_i][0] != 0:
        result_x = seq_x[dummy_i-1] + result_x
        result_y = "-" + result_y
        dummy_i -= 1
    while dummy_j !=0 and alignment_matrix[0][dummy_j] != 0:
        result_x = "-" + result_x
        result_y = seq_y[dummy_j-1] + result_y
        dummy_j -= 1
    return (result_score, result_x, result_y) 
