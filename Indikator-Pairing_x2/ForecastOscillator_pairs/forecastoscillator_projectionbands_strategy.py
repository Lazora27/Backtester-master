import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'ProjectionBands': 1.0
        })
    )
