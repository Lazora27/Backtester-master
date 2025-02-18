import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
