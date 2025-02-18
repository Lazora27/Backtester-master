import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und FisherSignals
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'FisherSignals': 1.0
        })
    )
