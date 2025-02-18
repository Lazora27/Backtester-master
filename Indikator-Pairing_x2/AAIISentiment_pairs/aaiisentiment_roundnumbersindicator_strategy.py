import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
