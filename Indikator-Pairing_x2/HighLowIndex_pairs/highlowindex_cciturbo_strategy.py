import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
