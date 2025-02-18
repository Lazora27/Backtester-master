import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'CCITurbo': 1.0
        })
    )
