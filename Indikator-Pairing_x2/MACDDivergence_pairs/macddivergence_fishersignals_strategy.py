import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'FisherSignals': 1.0
        })
    )
