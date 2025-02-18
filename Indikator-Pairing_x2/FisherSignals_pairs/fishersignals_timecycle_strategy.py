import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und TimeCycle
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'TimeCycle': 1.0
        })
    )
