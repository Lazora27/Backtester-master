import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'TrendCycles': 1.0
        })
    )
