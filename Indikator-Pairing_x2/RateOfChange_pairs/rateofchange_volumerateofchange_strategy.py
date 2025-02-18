import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
