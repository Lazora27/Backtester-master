import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'FisherSignals': 1.0
        })
    )
