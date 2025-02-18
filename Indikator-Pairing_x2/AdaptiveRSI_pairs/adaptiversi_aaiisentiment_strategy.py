import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'AAIISentiment': 1.0
        })
    )
