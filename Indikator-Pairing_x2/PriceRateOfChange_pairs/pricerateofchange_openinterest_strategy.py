import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und OpenInterest
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'OpenInterest': 1.0
        })
    )
