import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
