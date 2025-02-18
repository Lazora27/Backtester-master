import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'TickActivityIndex': 1.0
        })
    )
