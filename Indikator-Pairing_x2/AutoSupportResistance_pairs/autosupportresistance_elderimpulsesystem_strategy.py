import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
