import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'ParabolicSAR': 1.0
        })
    )
