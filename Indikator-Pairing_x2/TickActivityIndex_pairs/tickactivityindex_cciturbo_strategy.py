import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
