import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
