import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'WeightedCycle': 1.0
        })
    )
