import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'CycleFinder': 1.0
        })
    )
