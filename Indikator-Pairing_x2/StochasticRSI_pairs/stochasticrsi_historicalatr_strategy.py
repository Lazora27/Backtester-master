import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'HistoricalATR': 1.0
        })
    )
