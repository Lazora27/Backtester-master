import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
