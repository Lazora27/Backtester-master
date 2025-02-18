import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
