import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
