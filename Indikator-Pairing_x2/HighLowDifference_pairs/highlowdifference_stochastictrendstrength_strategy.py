import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
