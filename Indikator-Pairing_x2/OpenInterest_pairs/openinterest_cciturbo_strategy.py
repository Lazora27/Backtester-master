import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und CCITurbo
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'CCITurbo': 1.0
        })
    )
