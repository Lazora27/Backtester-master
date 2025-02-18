import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
