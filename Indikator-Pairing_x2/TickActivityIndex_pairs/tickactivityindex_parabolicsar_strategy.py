import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'ParabolicSAR': 1.0
        })
    )
