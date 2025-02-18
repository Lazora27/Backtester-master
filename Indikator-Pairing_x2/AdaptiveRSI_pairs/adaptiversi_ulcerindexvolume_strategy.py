import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
