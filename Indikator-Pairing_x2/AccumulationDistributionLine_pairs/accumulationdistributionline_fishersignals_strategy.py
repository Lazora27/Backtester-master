import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'FisherSignals': 1.0
        })
    )
