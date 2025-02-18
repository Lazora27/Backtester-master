import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
