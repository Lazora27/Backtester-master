import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und GannSquares
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'GannSquares': 1.0
        })
    )
