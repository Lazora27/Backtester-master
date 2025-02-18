import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'CycleFinder': 1.0
        })
    )
