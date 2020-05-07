 def sharpe(df, rate_free):
    #df é o dataframe com os dados
    #rate_free é a taxa livre de risco
    retorno = df['Close'].pct_change()
    desvio = retorno.std()
    return ((retorno[-1] - rate_free)/desvio)