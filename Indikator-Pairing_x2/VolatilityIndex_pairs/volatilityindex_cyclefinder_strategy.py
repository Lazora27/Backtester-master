import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
