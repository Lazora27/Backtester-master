import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'EaseOfMovement': 1.0
        })
    )
