import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
