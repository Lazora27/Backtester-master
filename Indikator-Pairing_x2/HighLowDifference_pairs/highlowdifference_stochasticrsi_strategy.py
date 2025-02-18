import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'StochasticRSI': 1.0
        })
    )
