import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'SmoothedCycle': 1.0
        })
    )
