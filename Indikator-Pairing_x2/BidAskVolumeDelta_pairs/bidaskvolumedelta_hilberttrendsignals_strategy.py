import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
