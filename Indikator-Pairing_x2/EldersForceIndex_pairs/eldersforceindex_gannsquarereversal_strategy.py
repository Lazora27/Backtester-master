import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'GannSquareReversal': 1.0
        })
    )
