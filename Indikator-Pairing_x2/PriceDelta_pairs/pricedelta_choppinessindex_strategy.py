import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
