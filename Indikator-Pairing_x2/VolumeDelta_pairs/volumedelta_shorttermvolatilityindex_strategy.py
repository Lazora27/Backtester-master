import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_ShortTermVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und ShortTermVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'ShortTermVolatilityIndex': {
                'class': ShortTermVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ShortTermVolatilityIndex'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'ShortTermVolatilityIndex': 1.0
        })
    )
