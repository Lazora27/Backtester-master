import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
