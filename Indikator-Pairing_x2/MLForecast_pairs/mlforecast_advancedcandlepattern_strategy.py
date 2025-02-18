import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
