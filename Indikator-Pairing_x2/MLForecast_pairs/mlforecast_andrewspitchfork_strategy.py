import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
