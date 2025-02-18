import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'LiquidityIndex': 1.0
        })
    )
