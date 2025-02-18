import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
