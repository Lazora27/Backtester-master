import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
