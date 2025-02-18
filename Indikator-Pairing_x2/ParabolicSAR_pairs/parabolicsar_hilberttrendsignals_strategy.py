import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
