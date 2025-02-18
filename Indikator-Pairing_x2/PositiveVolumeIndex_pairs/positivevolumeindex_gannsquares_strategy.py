import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und GannSquares
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'GannSquares': 1.0
        })
    )
