import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'PriceSquawk': 1.0
        })
    )
