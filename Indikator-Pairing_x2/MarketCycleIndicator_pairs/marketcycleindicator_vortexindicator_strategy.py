import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'VortexIndicator': 1.0
        })
    )
