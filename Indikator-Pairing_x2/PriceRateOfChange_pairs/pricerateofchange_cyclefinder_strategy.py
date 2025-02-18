import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und CycleFinder
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'CycleFinder': 1.0
        })
    )
