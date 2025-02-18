import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und SuperTrend
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'SuperTrend': 1.0
        })
    )
