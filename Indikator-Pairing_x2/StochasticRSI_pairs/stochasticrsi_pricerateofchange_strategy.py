import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
