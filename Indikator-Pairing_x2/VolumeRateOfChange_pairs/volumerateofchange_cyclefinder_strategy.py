import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und CycleFinder
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'CycleFinder': 1.0
        })
    )
