import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'StochasticOscillator': 1.0
        })
    )
