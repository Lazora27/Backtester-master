import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
