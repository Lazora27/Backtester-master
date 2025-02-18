import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
