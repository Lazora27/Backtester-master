import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
