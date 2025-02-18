import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
