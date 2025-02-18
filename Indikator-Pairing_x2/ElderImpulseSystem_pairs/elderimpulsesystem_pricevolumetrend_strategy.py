import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
