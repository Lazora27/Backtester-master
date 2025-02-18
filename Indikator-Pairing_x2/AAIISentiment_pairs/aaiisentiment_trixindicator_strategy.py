import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'TRIXIndicator': 1.0
        })
    )
