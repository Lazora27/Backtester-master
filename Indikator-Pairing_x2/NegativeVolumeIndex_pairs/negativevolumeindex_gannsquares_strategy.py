import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und GannSquares
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'GannSquares': 1.0
        })
    )
