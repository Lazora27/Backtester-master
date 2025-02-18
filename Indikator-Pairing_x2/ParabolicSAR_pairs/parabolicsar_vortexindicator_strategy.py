import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'VortexIndicator': 1.0
        })
    )
