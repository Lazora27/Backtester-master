import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
