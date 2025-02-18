import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und OpenInterest
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'OpenInterest': 1.0
        })
    )
