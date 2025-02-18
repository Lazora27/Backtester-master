import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
