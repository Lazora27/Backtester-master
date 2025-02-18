import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'ParabolicSAR': 1.0
        })
    )
