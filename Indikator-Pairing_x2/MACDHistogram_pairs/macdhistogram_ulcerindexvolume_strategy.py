import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
