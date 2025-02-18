import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
