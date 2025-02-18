import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
