import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
