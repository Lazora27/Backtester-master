import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'WeeklyCycle': 1.0
        })
    )
