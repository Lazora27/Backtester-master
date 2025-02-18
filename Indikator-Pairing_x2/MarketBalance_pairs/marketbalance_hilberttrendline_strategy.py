import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'HilbertTrendline': 1.0
        })
    )
