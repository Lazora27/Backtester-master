import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'FisherSignals': 1.0
        })
    )
