import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'ParabolicSAR': 1.0
        })
    )
