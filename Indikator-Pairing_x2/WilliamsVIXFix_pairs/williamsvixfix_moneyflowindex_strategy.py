import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
