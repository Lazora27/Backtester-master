import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'StochasticRSI': 1.0
        })
    )
