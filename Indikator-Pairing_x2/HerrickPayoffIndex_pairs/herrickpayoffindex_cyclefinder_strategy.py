import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
