import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'FlowOfFunds': 1.0
        })
    )
