import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
