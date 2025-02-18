import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'AverageTrueRange': 1.0
        })
    )
