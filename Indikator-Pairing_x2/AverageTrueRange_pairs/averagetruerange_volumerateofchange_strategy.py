import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
