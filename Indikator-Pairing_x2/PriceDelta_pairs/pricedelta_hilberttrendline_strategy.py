import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'HilbertTrendline': 1.0
        })
    )
