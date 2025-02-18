import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
