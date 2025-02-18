import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'VolumeProfile': 1.0
        })
    )
