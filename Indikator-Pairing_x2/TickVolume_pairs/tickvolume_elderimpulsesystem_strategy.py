import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
