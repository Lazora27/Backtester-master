import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
