import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
