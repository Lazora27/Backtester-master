import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'WeeklyCycle': 1.0
        })
    )
