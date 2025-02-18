import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedCycle_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedCycle und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'SmoothedCycle': 1.0,
            'WeightedCycle': 1.0
        })
    )
