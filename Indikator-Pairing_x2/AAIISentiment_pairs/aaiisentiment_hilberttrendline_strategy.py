import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'HilbertTrendline': 1.0
        })
    )
