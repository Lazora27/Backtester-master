import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
