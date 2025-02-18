import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'AdaptiveATR': 1.0
        })
    )
