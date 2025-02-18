import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
