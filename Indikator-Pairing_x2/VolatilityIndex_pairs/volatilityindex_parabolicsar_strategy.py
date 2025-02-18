import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'ParabolicSAR': 1.0
        })
    )
