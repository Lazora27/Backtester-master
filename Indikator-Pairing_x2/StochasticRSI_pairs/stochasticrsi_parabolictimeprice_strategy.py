import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
