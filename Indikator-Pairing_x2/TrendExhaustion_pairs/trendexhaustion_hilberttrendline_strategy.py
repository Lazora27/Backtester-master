import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'HilbertTrendline': 1.0
        })
    )
