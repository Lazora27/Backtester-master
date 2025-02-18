import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
