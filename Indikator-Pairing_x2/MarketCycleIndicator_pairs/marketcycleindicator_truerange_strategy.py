import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und TrueRange
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'TrueRange': 1.0
        })
    )
