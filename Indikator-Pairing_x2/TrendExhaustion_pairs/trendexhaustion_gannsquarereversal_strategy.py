import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'GannSquareReversal': 1.0
        })
    )
