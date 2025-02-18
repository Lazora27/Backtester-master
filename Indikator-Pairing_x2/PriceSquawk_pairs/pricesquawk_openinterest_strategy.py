import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und OpenInterest
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'OpenInterest': 1.0
        })
    )
