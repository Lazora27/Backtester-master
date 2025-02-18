import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
