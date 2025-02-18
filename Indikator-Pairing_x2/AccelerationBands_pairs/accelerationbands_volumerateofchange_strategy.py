import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
