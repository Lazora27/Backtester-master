import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'EhlersDecycler': 1.0
        })
    )
