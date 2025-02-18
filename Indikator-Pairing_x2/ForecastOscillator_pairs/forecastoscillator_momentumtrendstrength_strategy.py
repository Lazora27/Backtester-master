import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
