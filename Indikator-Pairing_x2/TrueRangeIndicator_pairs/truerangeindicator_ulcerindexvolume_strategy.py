import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
