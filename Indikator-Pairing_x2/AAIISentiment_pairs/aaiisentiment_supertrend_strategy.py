import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und SuperTrend
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'SuperTrend': 1.0
        })
    )
