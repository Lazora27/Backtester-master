import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und OpenInterest
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'OpenInterest': 1.0
        })
    )
