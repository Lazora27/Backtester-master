import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeeklyCycle_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeeklyCycle und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'WeeklyCycle': 1.0,
            'WeightedCycle': 1.0
        })
    )
