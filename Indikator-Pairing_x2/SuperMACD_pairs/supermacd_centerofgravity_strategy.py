import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'CenterOfGravity': 1.0
        })
    )
