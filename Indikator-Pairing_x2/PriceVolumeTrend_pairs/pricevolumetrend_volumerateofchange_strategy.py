import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
