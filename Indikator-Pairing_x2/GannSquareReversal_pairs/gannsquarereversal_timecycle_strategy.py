import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und TimeCycle
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'TimeCycle': 1.0
        })
    )
