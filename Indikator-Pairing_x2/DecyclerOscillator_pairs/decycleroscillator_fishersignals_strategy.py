import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DecyclerOscillator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DecyclerOscillator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'DecyclerOscillator': 1.0,
            'FisherSignals': 1.0
        })
    )
