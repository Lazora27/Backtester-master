import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'GannSquareReversal': 1.0
        })
    )
