import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und RateOfChange
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'RateOfChange': 1.0
        })
    )
