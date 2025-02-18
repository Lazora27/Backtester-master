import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
