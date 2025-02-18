import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'DPOCycles': 1.0
        })
    )
