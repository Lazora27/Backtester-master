import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'PriceSquawk': 1.0
        })
    )
