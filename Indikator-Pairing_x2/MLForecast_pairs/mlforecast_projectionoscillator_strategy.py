import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
