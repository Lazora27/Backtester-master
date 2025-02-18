import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'ExtensionProjections': 1.0
        })
    )
