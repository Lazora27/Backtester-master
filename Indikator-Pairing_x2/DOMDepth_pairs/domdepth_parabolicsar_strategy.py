import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'ParabolicSAR': 1.0
        })
    )
