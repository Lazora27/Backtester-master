import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
