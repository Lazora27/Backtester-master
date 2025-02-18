import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
