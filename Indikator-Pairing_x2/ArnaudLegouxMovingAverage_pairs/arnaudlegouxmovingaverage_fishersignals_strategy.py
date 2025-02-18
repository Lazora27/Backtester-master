import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArnaudLegouxMovingAverage_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArnaudLegouxMovingAverage und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ArnaudLegouxMovingAverage': {
                'class': ArnaudLegouxMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArnaudLegouxMovingAverage'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ArnaudLegouxMovingAverage': 1.0,
            'FisherSignals': 1.0
        })
    )
