import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'VortexIndicator': 1.0
        })
    )
