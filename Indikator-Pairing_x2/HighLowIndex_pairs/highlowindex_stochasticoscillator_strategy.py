import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'StochasticOscillator': 1.0
        })
    )
