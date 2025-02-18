import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'BuyingPressure': 1.0
        })
    )
