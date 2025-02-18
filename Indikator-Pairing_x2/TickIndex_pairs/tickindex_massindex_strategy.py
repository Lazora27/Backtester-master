import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und MassIndex
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'MassIndex': 1.0
        })
    )
