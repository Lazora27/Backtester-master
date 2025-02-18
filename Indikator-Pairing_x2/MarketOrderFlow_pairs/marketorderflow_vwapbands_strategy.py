import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und VWAPBands
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'VWAPBands': 1.0
        })
    )
