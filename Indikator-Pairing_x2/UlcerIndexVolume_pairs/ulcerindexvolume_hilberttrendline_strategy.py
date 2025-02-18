import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'HilbertTrendline': 1.0
        })
    )
