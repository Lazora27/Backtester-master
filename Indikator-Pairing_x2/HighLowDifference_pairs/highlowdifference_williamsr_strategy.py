import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und WilliamsR
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'WilliamsR': 1.0
        })
    )
