import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und WilliamsR
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'WilliamsR': 1.0
        })
    )
