import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und CCITurbo
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'CCITurbo': 1.0
        })
    )
