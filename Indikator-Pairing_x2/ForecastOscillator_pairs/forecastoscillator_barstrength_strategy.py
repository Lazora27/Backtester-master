import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und BarStrength
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'BarStrength': 1.0
        })
    )
