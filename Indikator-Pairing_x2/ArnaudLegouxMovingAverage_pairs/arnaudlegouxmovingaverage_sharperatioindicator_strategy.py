import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArnaudLegouxMovingAverage_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArnaudLegouxMovingAverage und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'ArnaudLegouxMovingAverage': {
                'class': ArnaudLegouxMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArnaudLegouxMovingAverage'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'ArnaudLegouxMovingAverage': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
