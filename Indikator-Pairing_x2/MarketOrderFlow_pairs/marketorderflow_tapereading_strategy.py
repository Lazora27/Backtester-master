import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und TapeReading
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'TapeReading': 1.0
        })
    )
