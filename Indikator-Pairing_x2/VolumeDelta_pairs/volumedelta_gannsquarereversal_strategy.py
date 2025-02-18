import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'GannSquareReversal': 1.0
        })
    )
