import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und FisherSignals
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'FisherSignals': 1.0
        })
    )
