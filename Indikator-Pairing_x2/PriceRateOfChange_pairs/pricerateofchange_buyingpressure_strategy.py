import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'BuyingPressure': 1.0
        })
    )
