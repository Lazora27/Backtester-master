import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'FisherSignals': 1.0
        })
    )
