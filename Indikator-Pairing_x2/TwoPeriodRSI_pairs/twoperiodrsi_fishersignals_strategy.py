import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und FisherSignals
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'FisherSignals': 1.0
        })
    )
