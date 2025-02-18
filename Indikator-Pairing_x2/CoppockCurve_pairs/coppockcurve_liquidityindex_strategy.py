import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'LiquidityIndex': 1.0
        })
    )
