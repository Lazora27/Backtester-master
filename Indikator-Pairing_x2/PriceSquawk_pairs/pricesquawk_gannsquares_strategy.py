import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und GannSquares
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'GannSquares': 1.0
        })
    )
