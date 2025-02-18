import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'MomentumIndicator': 1.0
        })
    )
