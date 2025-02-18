import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedCycle_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedCycle und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'SmoothedCycle': 1.0,
            'WeeklyCycle': 1.0
        })
    )
