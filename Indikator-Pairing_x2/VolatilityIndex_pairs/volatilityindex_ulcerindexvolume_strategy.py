import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
