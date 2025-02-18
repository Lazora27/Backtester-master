import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'AdaptiveATR': 1.0
        })
    )
