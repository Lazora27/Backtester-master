import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und CycleFinder
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'CycleFinder': 1.0
        })
    )
