import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und PriceDelta
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'PriceDelta': 1.0
        })
    )
