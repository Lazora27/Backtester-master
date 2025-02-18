import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und CCITurbo
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'CCITurbo': 1.0
        })
    )
