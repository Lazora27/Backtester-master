import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'TimeCycle': 1.0
        })
    )
