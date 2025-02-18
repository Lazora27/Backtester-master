import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'VortexIndicator': 1.0
        })
    )
