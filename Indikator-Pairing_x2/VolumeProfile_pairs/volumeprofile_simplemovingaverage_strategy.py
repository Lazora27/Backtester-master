import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
