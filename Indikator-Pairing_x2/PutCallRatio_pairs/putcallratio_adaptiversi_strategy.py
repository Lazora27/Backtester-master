import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
