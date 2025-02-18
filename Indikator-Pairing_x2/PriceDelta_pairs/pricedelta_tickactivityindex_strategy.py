import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'TickActivityIndex': 1.0
        })
    )
