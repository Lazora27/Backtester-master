import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ModifiedRSI': 1.0
        })
    )
