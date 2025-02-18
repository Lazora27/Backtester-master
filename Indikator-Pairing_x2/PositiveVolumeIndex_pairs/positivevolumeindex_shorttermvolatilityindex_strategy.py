import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_ShortTermVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und ShortTermVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'ShortTermVolatilityIndex': {
                'class': ShortTermVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ShortTermVolatilityIndex'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'ShortTermVolatilityIndex': 1.0
        })
    )
