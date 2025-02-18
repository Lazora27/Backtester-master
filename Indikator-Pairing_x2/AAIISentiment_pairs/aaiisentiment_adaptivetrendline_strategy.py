import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
