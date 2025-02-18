import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
