import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
