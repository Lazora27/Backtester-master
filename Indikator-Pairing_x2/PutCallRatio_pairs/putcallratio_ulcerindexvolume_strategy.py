import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
