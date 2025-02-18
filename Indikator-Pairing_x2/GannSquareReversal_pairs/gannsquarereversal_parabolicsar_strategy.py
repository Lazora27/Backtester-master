import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'ParabolicSAR': 1.0
        })
    )
