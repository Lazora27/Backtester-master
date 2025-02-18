import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und BarStrength
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'BarStrength': 1.0
        })
    )
