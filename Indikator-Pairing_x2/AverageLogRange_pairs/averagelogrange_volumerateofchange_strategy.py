import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
