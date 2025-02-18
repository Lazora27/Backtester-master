import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'StochasticOscillator': 1.0
        })
    )
