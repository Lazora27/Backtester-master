import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'ParabolicSAR': 1.0
        })
    )
