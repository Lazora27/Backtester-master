import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
