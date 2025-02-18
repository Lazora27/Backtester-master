import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'WeightedCycle': 1.0
        })
    )
