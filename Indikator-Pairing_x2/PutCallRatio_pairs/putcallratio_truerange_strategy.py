import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und TrueRange
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'TrueRange': 1.0
        })
    )
