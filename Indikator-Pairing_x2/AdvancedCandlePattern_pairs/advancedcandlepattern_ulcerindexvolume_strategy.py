import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
