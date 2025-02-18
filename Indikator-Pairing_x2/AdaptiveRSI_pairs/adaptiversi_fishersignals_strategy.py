import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'FisherSignals': 1.0
        })
    )
