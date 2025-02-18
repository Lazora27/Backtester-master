import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
