import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und OpenInterest
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'OpenInterest': 1.0
        })
    )
