import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'EaseOfMovement': 1.0
        })
    )
