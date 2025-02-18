import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ExtensionProjections': 1.0
        })
    )
