import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'ProjectionBands': 1.0
        })
    )
