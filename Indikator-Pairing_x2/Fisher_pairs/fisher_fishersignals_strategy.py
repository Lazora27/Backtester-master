import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und FisherSignals
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'FisherSignals': 1.0
        })
    )
