import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'ParabolicSAR': 1.0
        })
    )
