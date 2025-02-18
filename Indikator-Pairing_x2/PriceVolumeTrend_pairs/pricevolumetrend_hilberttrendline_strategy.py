import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'HilbertTrendline': 1.0
        })
    )
