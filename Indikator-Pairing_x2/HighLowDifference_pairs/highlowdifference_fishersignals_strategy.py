import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und FisherSignals
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'FisherSignals': 1.0
        })
    )
