import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und SuperMACD
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'SuperMACD': 1.0
        })
    )
