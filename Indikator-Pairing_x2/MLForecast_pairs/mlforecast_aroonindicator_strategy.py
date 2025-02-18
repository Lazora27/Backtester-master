import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'AroonIndicator': 1.0
        })
    )
