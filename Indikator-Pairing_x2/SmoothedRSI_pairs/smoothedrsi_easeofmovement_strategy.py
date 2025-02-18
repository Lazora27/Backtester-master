import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'EaseOfMovement': 1.0
        })
    )
