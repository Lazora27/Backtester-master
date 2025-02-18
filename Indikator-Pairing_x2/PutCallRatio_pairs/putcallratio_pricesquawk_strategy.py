import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'PriceSquawk': 1.0
        })
    )
