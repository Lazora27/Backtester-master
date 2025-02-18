import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
