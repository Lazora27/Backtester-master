import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
