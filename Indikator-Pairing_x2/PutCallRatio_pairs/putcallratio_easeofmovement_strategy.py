import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'EaseOfMovement': 1.0
        })
    )
