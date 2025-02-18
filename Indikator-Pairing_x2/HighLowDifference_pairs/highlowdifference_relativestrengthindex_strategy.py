import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
