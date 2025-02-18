import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'LiquidityIndex': 1.0
        })
    )
