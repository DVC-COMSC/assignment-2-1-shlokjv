def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    male = int(input('Enter number of male students: '))
    female = int(input('Enter number of female students: '))
    total = male + female
    m_perc = (male/total)*100
    f_perc = (female/total)*100
    print(f'The total number of students: \t\t {total}')
    print(f'The number of males and females \t {male} \t {female}')
    print(f'The percentage of males and females \t {m_perc:.2f}%\t {f_perc:.2f}%')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
