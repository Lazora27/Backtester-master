import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'WeightedCycle': 1.0
        })
    )
