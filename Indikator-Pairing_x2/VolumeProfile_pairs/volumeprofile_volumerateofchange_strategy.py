import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
