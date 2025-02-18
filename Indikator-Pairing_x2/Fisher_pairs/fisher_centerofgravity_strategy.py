import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'CenterOfGravity': 1.0
        })
    )
