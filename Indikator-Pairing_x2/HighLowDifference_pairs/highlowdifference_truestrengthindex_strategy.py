import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
