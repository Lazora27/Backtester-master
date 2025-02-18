import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'FlowOfFunds': 1.0
        })
    )
