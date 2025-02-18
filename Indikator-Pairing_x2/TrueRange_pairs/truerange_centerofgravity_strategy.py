import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'CenterOfGravity': 1.0
        })
    )
