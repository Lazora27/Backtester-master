import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'SeasonalStrength': 1.0
        })
    )
