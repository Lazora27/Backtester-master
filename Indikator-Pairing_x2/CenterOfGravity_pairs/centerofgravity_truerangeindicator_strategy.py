import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
