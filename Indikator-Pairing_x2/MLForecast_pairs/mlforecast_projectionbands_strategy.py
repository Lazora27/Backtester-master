import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ProjectionBands': 1.0
        })
    )
