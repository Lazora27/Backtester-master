import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und GannSquares
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'GannSquares': 1.0
        })
    )
