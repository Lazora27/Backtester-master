import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
