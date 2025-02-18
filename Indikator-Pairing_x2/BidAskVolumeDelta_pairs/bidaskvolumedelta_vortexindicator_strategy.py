import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'VortexIndicator': 1.0
        })
    )
