import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'TRIXIndicator': 1.0
        })
    )
