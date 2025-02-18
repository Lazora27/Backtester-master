import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und CycleFinder
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'CycleFinder': 1.0
        })
    )
