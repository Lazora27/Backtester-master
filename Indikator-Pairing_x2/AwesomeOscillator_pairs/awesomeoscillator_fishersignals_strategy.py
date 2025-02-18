import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'FisherSignals': 1.0
        })
    )
