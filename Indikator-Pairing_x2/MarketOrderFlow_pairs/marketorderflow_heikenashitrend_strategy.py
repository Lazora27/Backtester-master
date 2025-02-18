import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
