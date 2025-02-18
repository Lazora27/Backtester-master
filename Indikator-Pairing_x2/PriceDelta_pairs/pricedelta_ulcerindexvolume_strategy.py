import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
