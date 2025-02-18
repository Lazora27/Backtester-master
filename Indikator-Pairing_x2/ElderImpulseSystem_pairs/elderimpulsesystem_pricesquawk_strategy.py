import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'PriceSquawk': 1.0
        })
    )
