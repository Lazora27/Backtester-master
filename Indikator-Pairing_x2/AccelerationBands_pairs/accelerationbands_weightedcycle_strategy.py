import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'WeightedCycle': 1.0
        })
    )
