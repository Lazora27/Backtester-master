import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
