import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'WolfeWaves': 1.0
        })
    )
