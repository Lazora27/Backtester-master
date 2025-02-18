import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'LiquidityIndex': 1.0
        })
    )
