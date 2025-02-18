import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'WeightedCycle': 1.0
        })
    )
