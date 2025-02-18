import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'StochasticOscillator': 1.0
        })
    )
