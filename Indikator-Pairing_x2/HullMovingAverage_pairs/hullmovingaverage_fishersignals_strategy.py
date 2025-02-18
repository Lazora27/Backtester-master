import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und FisherSignals
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'FisherSignals': 1.0
        })
    )
