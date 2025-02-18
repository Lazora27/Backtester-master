import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
