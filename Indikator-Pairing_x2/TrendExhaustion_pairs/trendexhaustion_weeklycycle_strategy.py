import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'WeeklyCycle': 1.0
        })
    )
