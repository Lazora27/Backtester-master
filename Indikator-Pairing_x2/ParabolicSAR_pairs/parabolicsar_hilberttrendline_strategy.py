import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'HilbertTrendline': 1.0
        })
    )
