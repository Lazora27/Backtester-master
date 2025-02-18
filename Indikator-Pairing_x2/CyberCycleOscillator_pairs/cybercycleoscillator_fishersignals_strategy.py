import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycleOscillator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycleOscillator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'CyberCycleOscillator': 1.0,
            'FisherSignals': 1.0
        })
    )
