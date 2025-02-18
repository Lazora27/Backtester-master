import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
