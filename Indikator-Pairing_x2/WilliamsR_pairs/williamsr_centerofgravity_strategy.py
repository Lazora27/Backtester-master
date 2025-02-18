import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'CenterOfGravity': 1.0
        })
    )
