import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
