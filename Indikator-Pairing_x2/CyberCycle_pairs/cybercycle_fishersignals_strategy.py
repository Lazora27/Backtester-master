import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und FisherSignals
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'FisherSignals': 1.0
        })
    )
