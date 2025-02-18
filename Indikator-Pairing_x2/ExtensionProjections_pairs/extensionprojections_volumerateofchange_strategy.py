import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
