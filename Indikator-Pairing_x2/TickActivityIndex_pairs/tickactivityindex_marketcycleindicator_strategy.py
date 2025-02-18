import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
