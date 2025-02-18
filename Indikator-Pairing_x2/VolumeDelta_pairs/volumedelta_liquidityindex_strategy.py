import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'LiquidityIndex': 1.0
        })
    )
