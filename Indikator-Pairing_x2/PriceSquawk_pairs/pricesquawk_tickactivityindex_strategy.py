import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'TickActivityIndex': 1.0
        })
    )
