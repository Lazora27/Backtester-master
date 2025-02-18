import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'WeightedCycle': 1.0
        })
    )
