import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'UlcerIndex': 1.0
        })
    )
