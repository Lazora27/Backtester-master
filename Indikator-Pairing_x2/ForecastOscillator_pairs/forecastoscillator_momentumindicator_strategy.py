import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'MomentumIndicator': 1.0
        })
    )
