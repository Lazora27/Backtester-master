import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
