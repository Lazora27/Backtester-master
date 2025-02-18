import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'LiquidityIndex': 1.0
        })
    )
