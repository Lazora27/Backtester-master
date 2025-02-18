import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
