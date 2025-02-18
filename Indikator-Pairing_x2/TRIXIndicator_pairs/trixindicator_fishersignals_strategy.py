import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'FisherSignals': 1.0
        })
    )
