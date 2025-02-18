import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und GannSquares
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'GannSquares': 1.0
        })
    )
