import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
