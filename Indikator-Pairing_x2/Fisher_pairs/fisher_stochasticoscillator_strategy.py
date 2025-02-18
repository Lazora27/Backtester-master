import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'StochasticOscillator': 1.0
        })
    )
