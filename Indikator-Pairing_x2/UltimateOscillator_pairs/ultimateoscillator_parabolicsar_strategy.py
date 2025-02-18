import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'ParabolicSAR': 1.0
        })
    )
