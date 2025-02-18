import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'FisherSignals': 1.0
        })
    )
