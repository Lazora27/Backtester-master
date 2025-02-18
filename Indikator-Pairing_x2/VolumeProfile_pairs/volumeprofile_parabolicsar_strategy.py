import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'ParabolicSAR': 1.0
        })
    )
