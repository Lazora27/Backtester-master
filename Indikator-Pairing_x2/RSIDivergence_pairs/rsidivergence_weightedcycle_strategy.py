import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'WeightedCycle': 1.0
        })
    )
