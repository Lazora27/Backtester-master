import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
