import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
