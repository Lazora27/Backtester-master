import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'GannSquareReversal': 1.0
        })
    )
