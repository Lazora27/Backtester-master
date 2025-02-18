import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
