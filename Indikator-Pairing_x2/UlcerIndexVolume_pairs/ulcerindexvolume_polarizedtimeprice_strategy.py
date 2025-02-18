import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
