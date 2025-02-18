import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und TimeCycle
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'TimeCycle': 1.0
        })
    )
