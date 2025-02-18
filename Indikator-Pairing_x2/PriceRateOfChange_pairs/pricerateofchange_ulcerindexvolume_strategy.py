import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
