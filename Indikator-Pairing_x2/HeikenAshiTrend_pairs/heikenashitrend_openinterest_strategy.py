import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und OpenInterest
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'OpenInterest': 1.0
        })
    )
