import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
