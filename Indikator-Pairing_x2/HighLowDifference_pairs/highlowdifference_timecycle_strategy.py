import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und TimeCycle
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'TimeCycle': 1.0
        })
    )
