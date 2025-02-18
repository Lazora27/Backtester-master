import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'SmoothedCycle': 1.0
        })
    )
