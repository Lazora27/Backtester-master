import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'ParabolicSAR': 1.0
        })
    )
