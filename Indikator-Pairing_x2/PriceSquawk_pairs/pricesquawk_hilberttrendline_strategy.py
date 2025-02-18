import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'HilbertTrendline': 1.0
        })
    )
