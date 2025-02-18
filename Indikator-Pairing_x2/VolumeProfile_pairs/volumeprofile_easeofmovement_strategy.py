import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'EaseOfMovement': 1.0
        })
    )
