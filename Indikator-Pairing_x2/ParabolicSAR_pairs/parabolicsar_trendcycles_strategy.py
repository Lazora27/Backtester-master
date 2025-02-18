import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und TrendCycles
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'TrendCycles': 1.0
        })
    )
