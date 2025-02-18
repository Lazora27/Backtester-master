import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'AverageTrueRange': 1.0
        })
    )
