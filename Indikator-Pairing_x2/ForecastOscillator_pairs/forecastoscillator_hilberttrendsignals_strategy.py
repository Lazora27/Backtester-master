import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
