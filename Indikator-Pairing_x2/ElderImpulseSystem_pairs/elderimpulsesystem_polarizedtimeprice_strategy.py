import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
