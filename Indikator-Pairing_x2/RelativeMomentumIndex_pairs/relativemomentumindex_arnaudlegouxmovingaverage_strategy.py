import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_ArnaudLegouxMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und ArnaudLegouxMovingAverage
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'ArnaudLegouxMovingAverage': {
                'class': ArnaudLegouxMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArnaudLegouxMovingAverage'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'ArnaudLegouxMovingAverage': 1.0
        })
    )
