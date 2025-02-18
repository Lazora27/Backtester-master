import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
