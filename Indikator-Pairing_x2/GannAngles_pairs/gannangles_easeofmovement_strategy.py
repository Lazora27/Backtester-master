import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'EaseOfMovement': 1.0
        })
    )
