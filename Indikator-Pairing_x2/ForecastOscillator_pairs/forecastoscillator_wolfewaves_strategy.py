import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'WolfeWaves': 1.0
        })
    )
