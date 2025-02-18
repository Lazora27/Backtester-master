import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und TrueRange
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'TrueRange': 1.0
        })
    )
