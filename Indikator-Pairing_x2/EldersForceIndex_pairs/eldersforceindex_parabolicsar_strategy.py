import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'ParabolicSAR': 1.0
        })
    )
