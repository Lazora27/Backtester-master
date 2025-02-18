import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'ParabolicSAR': 1.0
        })
    )
