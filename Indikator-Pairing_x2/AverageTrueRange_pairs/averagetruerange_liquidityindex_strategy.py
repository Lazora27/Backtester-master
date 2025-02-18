import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'LiquidityIndex': 1.0
        })
    )
