import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'FlowOfFunds': 1.0
        })
    )
