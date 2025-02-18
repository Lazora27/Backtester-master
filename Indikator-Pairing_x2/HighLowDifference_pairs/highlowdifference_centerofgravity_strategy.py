import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'CenterOfGravity': 1.0
        })
    )
