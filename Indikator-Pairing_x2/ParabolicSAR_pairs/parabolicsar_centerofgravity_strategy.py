import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'CenterOfGravity': 1.0
        })
    )
