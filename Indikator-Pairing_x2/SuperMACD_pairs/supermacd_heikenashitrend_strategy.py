import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
