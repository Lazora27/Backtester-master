import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'UlcerIndex': 1.0
        })
    )
