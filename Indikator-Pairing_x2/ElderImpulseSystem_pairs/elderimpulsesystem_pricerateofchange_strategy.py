import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
