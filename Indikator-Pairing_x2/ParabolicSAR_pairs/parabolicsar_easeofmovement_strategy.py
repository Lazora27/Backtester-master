import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'EaseOfMovement': 1.0
        })
    )
