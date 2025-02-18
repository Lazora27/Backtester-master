import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
