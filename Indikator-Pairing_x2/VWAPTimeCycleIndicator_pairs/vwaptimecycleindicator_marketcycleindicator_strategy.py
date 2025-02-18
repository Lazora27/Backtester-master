import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPTimeCycleIndicator_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPTimeCycleIndicator und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'VWAPTimeCycleIndicator': {
                'class': VWAPTimeCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPTimeCycleIndicator'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'VWAPTimeCycleIndicator': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
