import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
