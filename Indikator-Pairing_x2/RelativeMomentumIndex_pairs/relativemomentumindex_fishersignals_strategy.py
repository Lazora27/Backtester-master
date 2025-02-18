import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
