import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und CCITurbo
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'CCITurbo': 1.0
        })
    )
