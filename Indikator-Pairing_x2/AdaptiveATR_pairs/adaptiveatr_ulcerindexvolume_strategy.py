import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
