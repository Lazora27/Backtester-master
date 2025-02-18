import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'FisherSignals': 1.0
        })
    )
