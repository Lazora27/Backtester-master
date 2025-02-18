import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'SmoothedRSI': 1.0
        })
    )
