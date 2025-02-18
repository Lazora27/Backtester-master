import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'SmoothedRSI': 1.0
        })
    )
