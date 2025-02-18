import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'EaseOfMovement': 1.0
        })
    )
