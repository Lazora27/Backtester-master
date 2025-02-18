import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und FisherSignals
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'FisherSignals': 1.0
        })
    )
