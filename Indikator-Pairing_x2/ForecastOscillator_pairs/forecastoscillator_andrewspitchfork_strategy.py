import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
