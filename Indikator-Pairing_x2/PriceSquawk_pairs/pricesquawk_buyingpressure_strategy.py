import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'BuyingPressure': 1.0
        })
    )
