import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'ParabolicSAR': 1.0
        })
    )
