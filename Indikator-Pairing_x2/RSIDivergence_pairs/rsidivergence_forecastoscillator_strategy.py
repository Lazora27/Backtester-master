import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ForecastOscillator': 1.0
        })
    )
