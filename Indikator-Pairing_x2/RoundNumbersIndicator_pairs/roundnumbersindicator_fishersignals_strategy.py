import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'FisherSignals': 1.0
        })
    )
