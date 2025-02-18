import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und FisherSignals
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'FisherSignals': 1.0
        })
    )
