import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'ParabolicSAR': 1.0
        })
    )
