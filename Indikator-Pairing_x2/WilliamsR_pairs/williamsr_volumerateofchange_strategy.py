import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
