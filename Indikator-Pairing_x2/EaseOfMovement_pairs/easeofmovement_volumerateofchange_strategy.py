import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
