import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'HullMovingAverage': 1.0
        })
    )
