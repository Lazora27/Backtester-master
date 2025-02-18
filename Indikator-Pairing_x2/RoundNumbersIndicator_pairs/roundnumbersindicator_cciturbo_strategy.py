import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'CCITurbo': 1.0
        })
    )
