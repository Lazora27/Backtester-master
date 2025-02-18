import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
