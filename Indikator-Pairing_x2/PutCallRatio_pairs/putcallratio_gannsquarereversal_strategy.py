import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'GannSquareReversal': 1.0
        })
    )
