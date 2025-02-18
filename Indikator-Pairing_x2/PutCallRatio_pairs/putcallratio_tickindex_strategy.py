import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_TickIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und TickIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'TickIndex': 1.0
        })
    )
