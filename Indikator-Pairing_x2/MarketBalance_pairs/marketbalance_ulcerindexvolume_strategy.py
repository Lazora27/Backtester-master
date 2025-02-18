import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
