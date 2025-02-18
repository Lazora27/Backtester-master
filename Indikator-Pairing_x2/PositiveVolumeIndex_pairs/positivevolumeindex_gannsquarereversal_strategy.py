import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'GannSquareReversal': 1.0
        })
    )
