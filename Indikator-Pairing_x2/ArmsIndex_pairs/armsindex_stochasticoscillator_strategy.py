import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'StochasticOscillator': 1.0
        })
    )
