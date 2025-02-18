import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_AdvanceDeclineRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und AdvanceDeclineRatio
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'AdvanceDeclineRatio': {
                'class': AdvanceDeclineRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineRatio'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'AdvanceDeclineRatio': 1.0
        })
    )
