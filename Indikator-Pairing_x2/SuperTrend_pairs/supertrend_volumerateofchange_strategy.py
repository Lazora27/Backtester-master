import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
