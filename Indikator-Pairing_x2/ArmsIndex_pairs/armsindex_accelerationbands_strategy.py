import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
