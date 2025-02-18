import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'HilbertTrendline': 1.0
        })
    )
