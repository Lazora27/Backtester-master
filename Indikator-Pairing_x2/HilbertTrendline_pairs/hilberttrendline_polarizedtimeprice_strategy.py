import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendline_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendline und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'HilbertTrendline': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
