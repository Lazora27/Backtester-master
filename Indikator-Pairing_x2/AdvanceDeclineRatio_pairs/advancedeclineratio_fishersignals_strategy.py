import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineRatio_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineRatio und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineRatio': {
                'class': AdvanceDeclineRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineRatio'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AdvanceDeclineRatio': 1.0,
            'FisherSignals': 1.0
        })
    )
