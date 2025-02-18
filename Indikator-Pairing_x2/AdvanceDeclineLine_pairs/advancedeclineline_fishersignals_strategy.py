import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'FisherSignals': 1.0
        })
    )
