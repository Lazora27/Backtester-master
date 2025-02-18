import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
