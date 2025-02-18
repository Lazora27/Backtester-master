import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
