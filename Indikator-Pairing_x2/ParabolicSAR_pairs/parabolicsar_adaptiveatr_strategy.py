import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'AdaptiveATR': 1.0
        })
    )
