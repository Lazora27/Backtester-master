import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'PriceSquawk': 1.0
        })
    )
