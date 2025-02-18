import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und MassIndex
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'MassIndex': 1.0
        })
    )
