import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'ExtensionProjections': 1.0
        })
    )
