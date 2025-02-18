import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
