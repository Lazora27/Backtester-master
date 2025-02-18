import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'PriceSquawk': 1.0
        })
    )
