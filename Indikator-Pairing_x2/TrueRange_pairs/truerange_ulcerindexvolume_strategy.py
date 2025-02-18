import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
