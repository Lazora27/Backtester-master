import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'BuyingPressure': 1.0
        })
    )
