import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
