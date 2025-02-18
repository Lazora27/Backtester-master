import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und GannSquares
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'GannSquares': 1.0
        })
    )
