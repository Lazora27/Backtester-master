import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
