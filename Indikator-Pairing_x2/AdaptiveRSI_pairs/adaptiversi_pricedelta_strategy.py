import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und PriceDelta
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'PriceDelta': 1.0
        })
    )
