import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und OpenInterest
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'OpenInterest': 1.0
        })
    )
