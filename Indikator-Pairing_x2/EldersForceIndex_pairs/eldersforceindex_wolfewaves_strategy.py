import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'WolfeWaves': 1.0
        })
    )
