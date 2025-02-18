import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'ParabolicSAR': 1.0
        })
    )
