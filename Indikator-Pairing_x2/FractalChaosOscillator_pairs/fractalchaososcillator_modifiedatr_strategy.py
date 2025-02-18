import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'ModifiedATR': 1.0
        })
    )
