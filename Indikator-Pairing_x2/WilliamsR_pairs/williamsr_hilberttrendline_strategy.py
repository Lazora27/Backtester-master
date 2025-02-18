import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'HilbertTrendline': 1.0
        })
    )
