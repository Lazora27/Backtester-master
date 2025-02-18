import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
