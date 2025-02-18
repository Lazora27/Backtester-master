import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
