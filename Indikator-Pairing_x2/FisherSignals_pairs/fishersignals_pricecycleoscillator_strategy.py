import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
