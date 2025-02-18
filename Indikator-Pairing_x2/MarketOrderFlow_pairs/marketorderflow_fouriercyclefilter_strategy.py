import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
