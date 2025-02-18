import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
