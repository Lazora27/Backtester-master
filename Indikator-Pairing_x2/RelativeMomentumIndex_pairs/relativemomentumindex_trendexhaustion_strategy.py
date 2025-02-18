import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'TrendExhaustion': 1.0
        })
    )
