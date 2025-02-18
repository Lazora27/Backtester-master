import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
