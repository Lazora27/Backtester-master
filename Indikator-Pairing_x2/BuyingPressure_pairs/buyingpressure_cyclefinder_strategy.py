import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und CycleFinder
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'CycleFinder': 1.0
        })
    )
