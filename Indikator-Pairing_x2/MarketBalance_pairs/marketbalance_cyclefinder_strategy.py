import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und CycleFinder
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'CycleFinder': 1.0
        })
    )
