import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
