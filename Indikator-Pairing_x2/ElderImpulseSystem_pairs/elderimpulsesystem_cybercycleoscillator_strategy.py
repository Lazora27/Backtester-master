import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
