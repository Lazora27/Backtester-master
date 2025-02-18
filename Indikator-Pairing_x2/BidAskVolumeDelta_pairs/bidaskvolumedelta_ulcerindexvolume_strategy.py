import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
