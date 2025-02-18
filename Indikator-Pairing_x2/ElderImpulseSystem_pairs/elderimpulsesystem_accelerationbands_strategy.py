import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'AccelerationBands': 1.0
        })
    )
