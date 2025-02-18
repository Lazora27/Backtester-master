import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und CycleFinder
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'CycleFinder': 1.0
        })
    )
