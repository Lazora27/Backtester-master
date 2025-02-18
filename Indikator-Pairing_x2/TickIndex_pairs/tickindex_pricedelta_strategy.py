import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und PriceDelta
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'PriceDelta': 1.0
        })
    )
