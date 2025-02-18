import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'WeeklyCycle': 1.0
        })
    )
