import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
