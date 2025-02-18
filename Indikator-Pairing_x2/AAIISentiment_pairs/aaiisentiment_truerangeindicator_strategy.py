import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
