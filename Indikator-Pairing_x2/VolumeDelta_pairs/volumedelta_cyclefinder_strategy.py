import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und CycleFinder
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'CycleFinder': 1.0
        })
    )
