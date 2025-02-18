import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'AccelerationBands': 1.0
        })
    )
