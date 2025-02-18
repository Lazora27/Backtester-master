import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
