import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
