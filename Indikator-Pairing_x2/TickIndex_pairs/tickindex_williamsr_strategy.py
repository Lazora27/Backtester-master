import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und WilliamsR
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'WilliamsR': 1.0
        })
    )
