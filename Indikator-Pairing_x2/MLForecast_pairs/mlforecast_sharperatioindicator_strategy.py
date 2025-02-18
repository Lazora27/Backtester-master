import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
