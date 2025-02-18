import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'GannSquareReversal': 1.0
        })
    )
