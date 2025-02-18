import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
