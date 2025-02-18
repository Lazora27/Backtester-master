import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'ParabolicSAR': 1.0
        })
    )
