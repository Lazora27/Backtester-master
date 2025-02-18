import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'VortexIndicator': 1.0
        })
    )
