import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'WeeklyCycle': 1.0
        })
    )
