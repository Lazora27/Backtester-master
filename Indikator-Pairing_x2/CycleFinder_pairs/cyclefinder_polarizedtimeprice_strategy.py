import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
