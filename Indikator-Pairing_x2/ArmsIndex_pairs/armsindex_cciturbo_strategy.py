import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
