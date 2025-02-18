import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
